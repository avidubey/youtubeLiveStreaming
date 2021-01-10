# RTSP Variables
# Replace the following with your own values before running the script

echo "Starting live streaming !!"
ffmpeg -fflags +igndts -i $RTSP_URL -c:a copy  -filter:v fps=fps=2 -f flv  $RTMP_URL 
