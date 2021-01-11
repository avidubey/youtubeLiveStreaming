
# What is the end goal?
Setup Youtube live streaming using a webcam that supports RTSP and raspberry pi. Setup in a way that it saves bandwidth during non-active hours.

# What all things we need?
1. A webcam that supports RTSP (without any SD card). This allows to keep the webcam near the video input source needing just one power setup. Such setup is usually outside the house like bird feeder, home security, etc. 
2. An additional compute like raspberry pi can be kept inside the house with wifi connectivity to host the compute for converting RTSP into RTMP.

# Which camera did I use?
I used wyze cam V2 for this : https://wyze.com/wyze-cam.html 

# Why do we need to convert RTSP into RTMP?
Youtube only supports RTMP

# What are the steps for this setup?
## Setup wyze cam using the app
Wyze cam like other wifi cams comes with its own app. Use it to setup and connect to local wifi. Make sure you are able to watch the live stream on the wyze cam app first.

## Setup RTSP on wyze cam
This is an important step. Although this feature is in beta, but it works quite well. In order to setup RTSP follow the following instructions provided by wyze : 
But please read the instructions before setting this up as you might lose future functionalities in the wyze app. I did not care and bought wyze cam for live streaming purpose. 
"RTSP is not a stock feature with the Wyze Cam and is a beta feature that requires the installation of different firmware.  Using the RTSP firmware will prevent the camera from supporting any future functions or features in the Wyze app."

## Setup a raspberry pi (or raspberry pi zero). You can use any compute like mac, windows, linux, I used raspberry pi zero so that I can have a cheap dedicated hardware always running for live streaming.
This is a common setup instruction which keeps on evolving with time. I used raspberry Pi imager on mac to do the setup on SD card : Please refer to official documentation for raspberry pi setup : https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2 

## Confirm/Install ffmpeg on raspberry pi
The default setup of raspberry pi comes with ffmpeg so try the following command
Run ffmpeg to try out if its there or not and you should get an output like this
```
pi@raspberrypi:~ $ ffmpeg
ffmpeg version 4.1.6-1~deb10u1+rpt1 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 8 (Raspbian 8.3.0-6+rpi1)
  configuration: <long list of configuration commands here>
```

If it says command not found then either you don't have ffmpeg or its not in your command path
```
-bash: ffmpeg: command not found
```
In that case please install ffmpeg using the following command

```
sudo apt install ffmpeg
```

## Setup Youtube for starting live streaming
<TODO>
  
## Start streaming RTSP feed from webcam to RTMP endpoint of Youtube
Just run ./fastStream.sh to start streaming on youtube. The reason behind fastStream and slowStream is explained later


# Why slow streaming at night and fast streaming during day time?
Created two different files which have commands to start the streaming using ffmpeg. fastStream for day time and slowStream for night time. 

The slow streaming is for saving bandwidth during night time when there is little to no action of birds. No point streaming at higher fps
With youtube if the live streaming is stopped, it would end the stream and it needs manual intervention to restart the stream using website
Hence, the slow streaming keeps the youtube stream alive as well as saves bandwidth as we are streaming just 1 frame per second.

# Cron setup for automated start of streaming
Add the following lines in your cron file
Type ``` crontab -e ```
and add the following lines to start fast streaming in daytime and slow streaming in night time
```
0 6 * * * timeout 11h /home/pi/workspace/youtubeLiveStreaming/fastStream.sh > /dev/null 2>&1
0 17 * * * timeout 13h /home/pi/workspace/youtubeLiveStreaming/slowStream.sh > /dev/null 2>&1
```
