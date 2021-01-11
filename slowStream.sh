#!/bin/bash -l

##
# The slow streaming is for saving bandwidth during night time when there is little to no action of birds. No point streaming at higher fps
# With youtube if the live streaming is stopped, it would end the stream and it needs manual intervention to restart the stream using website
# The slow streaming keeps the youtube stream alive as well as saves bandwidth as we are streaming just 1 frame per second.
##

# ENVIRONMENT VARIABLES
# Expecting RTSP_URL and RTMP_URL environment variables setup in the system. Please read README file for instructions and steps

echo "Killing existing ffmpeg first for clean up and fresh start"
killall ffmpeg
echo "Starting slow live streaming to just keep live streaming alive!!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:a copy -filter:v fps=1 -g 4 -f flv $RTMP_URL
