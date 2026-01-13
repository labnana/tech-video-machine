import os
from moviepy.editor import *

# Paths
SCRIPT_TEXT = "output/script.txt"
VOICE_PATH = "output/voice.wav"
BG_MUSIC = "assets/tech_bg.mp3"
OUTPUT_DIR = "output/final"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Base video (simple animated background)
bg = ColorClip(size=(1920,1080), color=(15,23,42), duration=60)

# Voice
voice = AudioFileClip(VOICE_PATH)

# Background music (low volume)
if os.path.exists(BG_MUSIC):
    music = AudioFileClip(BG_MUSIC).volumex(0.15)
    audio = CompositeAudioClip([voice, music])
else:
    audio = voice

# Text animation
title = TextClip(
    "Tech Explained",
    fontsize=80,
    color="white",
    font="Arial-Bold"
).set_duration(5).set_position("center").crossfadein(1)

final = CompositeVideoClip([bg, title])
final = final.set_audio(audio)

# Export
final.write_videofile(
    f"{OUTPUT_DIR}/tech_video_final_1080p.mp4",
    fps=30,
    codec="libx264",
    audio_codec="aac"
)

print("✅ FINAL VIDEO READY")
