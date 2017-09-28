# splunkDeepfreeze
Move frozen buckets to AWS S3 (and ultimately Glacier) for long term storage

This tool provides 2 scripts:

## cold2frozen.py
Copy this file to app/bin
This script can be configured as your frozen script. It will take buckets which have expired the cold lifecycle, and will move the data outside of the splunk db path to a location of your choosing - you will need to edit the script to set the paths

## frozen2deepfreeze.py
Copy this file to app/bin
This script runs as a scripted input and moves the contents of the frozen path into s3 - you will need to edit the script to set the paths

## inputs.conf 
Copy this file to an app/default folder to enable the scripted input

If this script works for you, or you would like to see it built into a full app, please let me know how you get on!
