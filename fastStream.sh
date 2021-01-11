#!/bin/bash


# ENVIRONMENT VARIABLES
# Expecting RTSP_URL and RTMP_URL environment variables setup in the system. Please read README file for instructions and steps
# Using default input fps as output fps

echo "Starting slow live streaming to just keep live streaming alive!!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:v copy -c:a copy -f flv -f flv  $RTMP_URL
