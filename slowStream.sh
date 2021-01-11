#!/bin/bash


# ENVIRONMENT VARIABLES
# Expecting RTSP_URL and RTMP_URL environment variables setup in the system. Please read README file for instructions and steps
# The slow streaming is for saving bandwidth during night time when there is little to no action of birds. No point streaming at higher fps
# With youtube if the live streaming is stopped, it would end the stream and it needs manual intervention to restart the stream using website
# The slow streaming keeps the youtube stream alive as well as saves bandwidth as we are streaming just 1 frame per second.

FPS = 1
echo "Starting slow live streaming to just keep live streaming alive!!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:a copy -filter:v fps=fps=1 -g 60 -f flv  $RTMP_URL 
