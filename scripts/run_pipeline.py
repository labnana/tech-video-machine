import subprocess
import os

print("🚀 Tech Video Machine Pipeline Started")

os.makedirs("outputs/videos_shorts", exist_ok=True)
os.makedirs("outputs/videos_long", exist_ok=True)

print("🔊 Generating voices...")
subprocess.run(["python", "scripts/generate_voice.py"], check=True)

print("🎬 Building SHORT video...")
subprocess.run(["bash", "scripts/build_short_video.sh"], check=True)

print("🎞️ Building LONG video...")
subprocess.run(["bash", "scripts/build_long_video.sh"], check=True)

print("✅ Pipeline finished successfully")
