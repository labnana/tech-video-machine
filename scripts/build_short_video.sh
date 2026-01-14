#!/bin/bash

VOICE="outputs/voices/voice_short_de.wav"
BROLL="outputs/broll/*.mp4"
OUT="outputs/videos_shorts/tech_short_final.mp4"

ffmpeg \
 -stream_loop -1 -i $BROLL \
 -i $VOICE \
 -filter_complex "
 [0:v]scale=1080:1920,zoompan=z='min(zoom+0.001,1.2)':d=90,setsar=1[v]
 " \
 -map "[v]" -map 1:a \
 -c:v libx264 -preset fast -crf 20 \
 -pix_fmt yuv420p \
 -shortest \
 $OUT

echo "SHORT VIDEO READY"
