import os
import subprocess

SCRIPT_FILE = "outputs/scripts/script_long_de.txt"
VOICE_OUT = "outputs/voices/voice_long_de.wav"

os.makedirs("outputs/voices", exist_ok=True)

# Coqui TTS command
command = [
    "tts",
    "--text_file", SCRIPT_FILE,
    "--model_name", "tts_models/de/thorsten/tacotron2-DDC",
    "--out_path", VOICE_OUT
]

subprocess.run(command, check=True)

print("✅ German Voice Generated:", VOICE_OUT)
