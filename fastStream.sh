#!/bin/bash -l

##
# Use this script to stream at regular high quality bandwidth. The cron job in my setup runs this script during day time and slowStream.sh script during night
# when there is no activity. This helps saves bandwidth cost.
##

# ENVIRONMENT VARIABLES
# Expecting RTSP_URL and RTMP_URL environment variables setup in the system. Please read README file for instructions and steps
# Using default input fps as output fps
echo "Killing existing ffmpeg first for clean up and fresh start"
killall ffmpeg
echo "Starting slow live streaming to just keep live streaming alive!!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:v copy -c:a copy -f flv $RTMP_URL
