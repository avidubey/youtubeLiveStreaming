# Put this script as start up script so in case raspbery pi restarts, it would keep the youtube stream running.
# This script automatically figures out if its day time or night time based on the location and starts fast/slow stream accordingly

import os
import sys
import requests
import json
from datetime import datetime, time, timedelta, timezone

# Get RTSP_URL and RTMP_URL from environment variables
# These will be unique to your use cases but would look something like this
# RTSP_URL = "rtsp://username:password@cameraIP/live" for your wyze cam
# RTMP_URL = "rtmp://a.rtmp.youtube.com/live2/<your stream key here>"
os.system('#!/bin/bash -l')
RTSP_URL = os.environ['RTSP_URL']
RTMP_URL = os.environ['RTMP_URL']

# Get your location's environment variables from https://sunrise-sunset.org/api
lattitude = 47.6694141
longitude = -122.1238767

# Get sunrise and sunset time from https://sunrise-sunset.org
url = f'https://api.sunrise-sunset.org/json?lat={lattitude}&lng={longitude}&formatted=0' # URL, change lat and lng
print(url)
r = requests.get(url) # query data
print(r)

d = datetime.now(timezone.utc)
today_date = d.date()
time_now = d.time()
data = json.loads(r.content)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_time = time(int(sunrise[11:13]), int(sunrise[14:16])) # Change sunrise in time format
sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) # Change sunset into time format

print("Killing existing processes first to avoid duplicate processes")
os.system('killall ffmpeg')

# Check if there is override argument to run specifically for day time or night time
# example : override for day time : python3 autoStream.py true
# example : override for night time : python3 autoStream.py false
isDaytime = 0
if len(sys.argv) > 1:
	isDaytime = sys.argv[1]
	print(f'override daytime flag set as {isDaytime}')

print(f'time_now {time_now}, sunrise_time {sunrise_time}, sunset_time {sunset_time} ')

if (isDaytime == '1') or (time_now > sunrise_time and time_now < sunset_time):  # In between sunrise and sunse
	print("Starting fast streaming as its day time")
	os.system(f'ffmpeg -fflags +igndts -i {RTSP_URL} -c:v copy -c:a copy -f flv {RTMP_URL}')
else:
	print("Starting slow streaming as its night time")
	os.system(f'ffmpeg -fflags +igndts -i {RTSP_URL} -c:a copy -filter:v fps=1 -g 4 -f flv {RTMP_URL}')
