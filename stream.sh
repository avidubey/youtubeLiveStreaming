# RTSP Variables
# Replace the following with your own values before running the script
RTSP_URL = <rtsp url from your wyze app. It would look something like rtsp://someUserName:somePassword@SomeIp/live>

# If you are not using wyze and some other wifi cam then the rtsp link might look like rtsp://username:password@someIp:554

# Youtube's RTMP Variables
RTMP_URL = rtmp://a.rtmp.youtube.com/live2
RTMP_STREAM_KEY = <your secret youtube stream key, DO NOT SHARE THIS WITH OTHERS>

echo "Starting live streaming !!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:v copy -c:a copy -f flv $RTMP_URL/$RTMP_STREAM_KEY

