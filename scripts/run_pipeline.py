import subprocess
from pathlib import Path

print("Starting pipeline...")

# Step 1: Generate voice
subprocess.run(["python", "scripts/generate_voice.py"], check=True)

# Step 2: Build short video
subprocess.run(["bash", "scripts/build_short_video.sh"], check=True)

print("Pipeline finished successfully")
