# Put this script as start up script so in case raspbery pi restarts, it would keep the youtube stream running.
# This script automatically figures out if its day time or night time based on the location and starts fast/slow stream accordingly

import os
import requests
import json
from datetime import datetime, time, timedelta

# Get RTSP_URL and RTMP_URL from environment variables
# These will be unique to your use cases but would look something like this
# RTSP_URL = "rtsp://username:password@cameraIP/live" for your wyze cam
# RTMP_URL = "rtmp://a.rtmp.youtube.com/live2/<your stream key here>"

# Get your location's environment variables from https://sunrise-sunset.org/api
lattitude = 47.6694141
longitude = -122.1238767

# Get sunrise and sunset time from https://sunrise-sunset.org
url = f'https://api.sunrise-sunset.org/json?lat={lattitude}&lng={longitude}&formatted=0' # URL, change lat and lng
print(url)
r = requests.get(url) # query data
print(r)

d = datetime.now()
today_date = d.date()
time_now = d.time()
data = json.loads(r.content)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_time = time(int(sunrise[11:13]), int(sunrise[14:16])) # Change sunrise in time format
sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) # Change sunset into time format

print("Killing existing processes first to avoid duplicate processes")
os.system('killall ffmpeg')

if time_now > sunrise_time and time_now < sunset_time:  # In between sunrise and sunset, so run faster stream	
	print("Starting fast streaming as its day time")
	os.system('ffmpeg -fflags +igndts -i $RTSP_URL -c:a copy -filter:v -f flv $RTMP_URL')
else:
	print("Starting slow streaming as its night time")
	os.system('ffmpeg -fflags +igndts -i $RTSP_URL -c:a copy -filter:v fps=1 -g 4 -f flv $RTMP_URL')
