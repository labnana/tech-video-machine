import json
import os
from gtts import gTTS

INPUT_FILE = "inputs/topics.json"
OUTPUT_DIR = "outputs/voices"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    topics = json.load(f)

for item in topics:
    vid = item["id"]
    text = item["topic"]

    out_file = f"{OUTPUT_DIR}/voice_{vid}.wav"

    tts = gTTS(text=text, lang="de")
    tts.save(out_file)

    print(f"✅ Voice generated: {out_file}")
