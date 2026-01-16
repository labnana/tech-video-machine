import os
from gtts import gTTS

os.makedirs("outputs/voices", exist_ok=True)

def make_voice(text, out):
    tts = gTTS(text=text, lang="de")
    tts.save(out)
    print(f"✅ Voice created: {out}")

# ~60 sec
SHORT_TEXT = "Dies ist ein kurzes Tech Video. " * 30

# ~5–6 min
LONG_TEXT = "Dies ist ein langes Tech Video. " * 180

make_voice(SHORT_TEXT, "outputs/voices/voice_short_de.wav")
make_voice(LONG_TEXT,  "outputs/voices/voice_long_de.wav")
