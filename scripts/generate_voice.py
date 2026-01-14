from gtts import gTTS
import os

INPUT_TOPIC_FILE = "inputs/topic_001/topic.txt"
OUTPUT_DIR = "outputs/voices"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "voice_de.wav")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_TOPIC_FILE, "r", encoding="utf-8") as f:
    text = f.read()

tts = gTTS(text=text, lang="de")
tts.save(OUTPUT_FILE)

print(f"Voice generated successfully at {OUTPUT_FILE}")
