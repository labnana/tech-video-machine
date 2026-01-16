#!/bin/bash
set -e

ffmpeg -y \
-i outputs/broll/sample.mp4 \
-i outputs/voices/voice_long_de.wav \
-stream_loop 5 \
-shortest \
-c:v libx264 -pix_fmt yuv420p \
-c:a aac \
outputs/videos_long/long_001.mp4
