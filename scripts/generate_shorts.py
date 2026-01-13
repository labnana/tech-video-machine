import os
from moviepy.editor import *

# Paths
VOICE_PATH = "output/voice.wav"
BG_MUSIC = "assets/tech_bg.mp3"
OUTPUT_DIR = "output/final"

os.makedirs(OUTPUT_DIR, exist_ok=True)

DURATION = 60  # Shorts length

# Vertical background (9:16)
bg = ColorClip(
    size=(1080,1920),
    color=(10,15,30),
    duration=DURATION
)

# Voice
voice = AudioFileClip(VOICE_PATH).subclip(0, DURATION)

# Background music (soft)
if os.path.exists(BG_MUSIC):
    music = AudioFileClip(BG_MUSIC).volumex(0.12).subclip(0, DURATION)
    audio = CompositeAudioClip([voice, music])
else:
    audio = voice

# Animated Text (CapCut style)
headline = TextClip(
    "AI Tech erklärt 🚀",
    fontsize=90,
    color="white",
    font="Arial-Bold",
    method="caption",
    size=(900,None)
).set_position(("center","center")).set_duration(5).crossfadein(0.5)

video = CompositeVideoClip([bg, headline])
video = video.set_audio(audio)

# Export
video.write_videofile(
    f"{OUTPUT_DIR}/tech_short_final_9x16.mp4",
    fps=30,
    codec="libx264",
    audio_codec="aac"
)

print("✅ SHORT VIDEO READY")
