from gtts import gTTS
from pathlib import Path

# Read topic script
script_path = Path("inputs/topic_001/topic.txt")
text = script_path.read_text(encoding="utf-8")

# German male-style voice (gTTS limitation: gender simulated via params)
tts = gTTS(
    text=text,
    lang="de",
    slow=False
)

output_dir = Path("outputs/voices")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "voice_de_male.wav"
tts.save(str(output_file))

print(f"Male German voice generated: {output_file}")
