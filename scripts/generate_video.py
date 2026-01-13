import subprocess
from pathlib import Path

BASE = Path(__file__).parent.parent
VOICE = BASE / "voices" / "voice_de.wav"
OUT = BASE / "output" / "final"
OUT.mkdir(parents=True, exist_ok=True)

VIDEO = OUT / "tech_video_1080p.mp4"

print("🎬 Creating video with FFmpeg...")

subprocess.run([
    "ffmpeg",
    "-y",
    "-f", "lavfi",
    "-i", "color=c=black:s=1920x1080:d=60",
    "-i", str(VOICE),
    "-vf",
    "drawtext=text='German Tech Explained':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h-text_h)/2",
    "-shortest",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    str(VIDEO)
])

print("✅ Video created:", VIDEO)
