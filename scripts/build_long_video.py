from moviepy.editor import *
import os

SCRIPT_DURATION_MIN = 20  # auto scalable (2–40)
OUTPUT_DIR = "outputs/long_videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Dummy base clip (placeholder visuals)
base_clip = ColorClip(
    size=(1920,1080),
    color=(15,23,42),
    duration=SCRIPT_DURATION_MIN * 60
)

# Text overlay (simulating tech captions)
txt = TextClip(
    "German Tech Review\nProfessionell erklärt",
    fontsize=70,
    color="white",
    size=(1800,None),
    method="caption"
).set_position("center").set_duration(10)

video = CompositeVideoClip([base_clip, txt])

# Light zoom effect
video = video.fx(vfx.resize, lambda t: 1 + 0.02*t)

# Export
output_path = f"{OUTPUT_DIR}/long_tech_video.mp4"
video.write_videofile(
    output_path,
    fps=30,
    codec="libx264",
    audio=False
)

print("✅ LONG VIDEO READY:", output_path)
