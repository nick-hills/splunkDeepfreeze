#! /usr/bin/python

# This is based on the splunk example script, but removes
# much of the unnecessary complication for older versions.
# This script is tested on Splunk 6.x on Linux. (Windows may need tweaking)

######## NOTE #######
# You MUST configure one of the following options

# If you want a path relative to splunk home, use the follwing format:
#ARCHIVE_DIR = os.path.join(os.getenv('SPLUNK_HOME'), 'frozenData')

# -or-

# Simply use a full base path like:
#ARCHIVE_DIR = '/opt/frozenData'



import sys, os, gzip, shutil, subprocess, random

def archiveBucket(base, files):
    print 'Archiving bucket: ' + base
    for f in files:
        full = os.path.join(base, f)
        if os.path.isfile(full):
            os.remove(full)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: python cold2frozen.py <bucket_path>')

    if not os.path.isdir(ARCHIVE_DIR):
        try:
            os.mkdir(ARCHIVE_DIR)
        except OSError:
            sys.stderr.write("mkdir warning: Directory '" + ARCHIVE_DIR + "' already exists\n")

    bucket = sys.argv[1]
    if not os.path.isdir(bucket):
        sys.exit('Given bucket is not a valid directory: ' + bucket)

    rawdatadir = os.path.join(bucket, 'rawdata')
    if not os.path.isdir(rawdatadir):
        sys.exit('No rawdata directory, given bucket is likely invalid: ' + bucket)

    files = os.listdir(bucket)
    journal = os.path.join(rawdatadir, 'journal.gz')
    if os.path.isfile(journal):
        archiveBucket(bucket, files)
    else:
        sys.exit('No journal file found, bucket invalid:' + bucket)

    if bucket.endswith('/'):
        bucket = bucket[:-1]

    indexname = os.path.basename(os.path.dirname(os.path.dirname(bucket)))
    destdir = os.path.join(ARCHIVE_DIR, indexname, os.path.basename(bucket))

    while os.path.isdir(destdir):
        print 'Warning: This bucket already exists in the archive directory'
        print 'Adding a random extension to this directory...'
        destdir += '.' + str(random.randrange(10))

    shutil.copytree(bucket, destdir)
