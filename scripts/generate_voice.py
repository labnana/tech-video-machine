import os
from pathlib import Path
import subprocess

BASE = Path(__file__).parent.parent
SCRIPT_DIR = BASE / "scripts"
VOICE_DIR = BASE / "voices"

VOICE_DIR.mkdir(exist_ok=True)

# latest script pick karo
scripts = sorted(SCRIPT_DIR.glob("script_*.txt"))
if not scripts:
    raise Exception("❌ No script found")

script_text = scripts[-1].read_text(encoding="utf-8")

output_voice = VOICE_DIR / "voice_de.wav"

print("🎤 Generating German voice...")

subprocess.run([
    "tts",
    "--text", script_text,
    "--model_name", "tts_models/de/thorsten/tacotron2-DDC",
    "--out_path", str(output_voice)
])

print("✅ Voice generated:", output_voice)
