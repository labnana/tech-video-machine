#!/bin/bash
set -e

ffmpeg -y \
-i outputs/broll/sample.mp4 \
-i outputs/voices/voice_short_de.wav \
-shortest \
-c:v libx264 -pix_fmt yuv420p \
-c:a aac \
outputs/videos_shorts/short_001.mp4
