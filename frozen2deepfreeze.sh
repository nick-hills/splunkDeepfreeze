#! /bin/bash

# This script is designed to be run on a system with the AWS command line tools
# correctly installed and configured, including  configured keys and bucket permissions.
# ...or from an AWS instance with IAM roles etc.

# If you need to specify a proxy uncomment and complete the following
#export HTTPS_PROXY=http://a.b.c.d:3128

ARCHIVE_DIR='/opt/frozenData'
S3_ARCHIVE_BUCKET='your-bucket-name'
S3_REGION='eu-west-1'

cd $ARCHIVE_DIR
for file in $(find . -name '*.gz'); 
do 
	relativepath=$(echo $file |sed 's/\.\///')
	bucketdetails=$(echo $relativepath|awk -F/ '{print "index="$1 " bucket="$2}')
	timestarted=$(date --utc +%FT%TZ)
	/usr/bin/aws s3 cp $file s3://$S3_ARCHIVE_BUCKET/$relativepath --region $S3_REGION --sse --only-show-error
	
	if [ $? -eq 0 ]; then
		folder=$(echo $file|sed -e 's,/rawdata/journal.gz,,')
		rm -rf $folder
		res='success'
	else
		res='failure'
	fi
	
	echo $timestarted DeepFreezing $bucketdetails result=$res
done
