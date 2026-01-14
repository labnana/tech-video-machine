#!/bin/bash

VOICE="outputs/voices/voice_long_de.wav"
MUSIC="outputs/music/tech_bg.mp3"
BROLL="outputs/broll/*.mp4"
OUT="outputs/videos_long/tech_long_final.mp4"

ffmpeg \
 -stream_loop -1 -i $BROLL \
 -i $VOICE \
 -i $MUSIC \
 -filter_complex "
 [0:v]scale=1920:1080,zoompan=z='min(zoom+0.0005,1.1)':d=125,fade=t=in:st=0:d=1,fade=t=out:st=5:d=1[v];
 [2:a]volume=0.08[a2];
 [1:a][a2]amix=inputs=2:dropout_transition=2[a]
 " \
 -map "[v]" -map "[a]" \
 -c:v libx264 -preset slow -crf 18 \
 -pix_fmt yuv420p \
 -shortest \
 $OUT

echo "LONG VIDEO READY"
