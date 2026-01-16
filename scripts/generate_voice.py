from gtts import gTTS
from pathlib import Path

# Read topic text (FULL file)
topic_file = Path("inputs/topic_001/topic.txt")
text = topic_file.read_text(encoding="utf-8")

# Generate German voice
tts = gTTS(
    text=text,
    lang="de",
    slow=False
)

output_dir = Path("outputs/voices")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "voice_de.wav"
tts.save(str(output_file))

print(f"Voice generated successfully at {output_file}")
