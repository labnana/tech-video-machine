from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent

SCRIPT_DIR = BASE / "scripts"
VOICE_DIR = BASE / "voices"
OUTPUT_DIR = BASE / "output"

SCRIPT_DIR.mkdir(exist_ok=True)
VOICE_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

topic = "KI Tools für Produktivität"

script_text = f"""
TITEL: {topic} – Tech Analyse 2026

HOOK:
Wusstest du, dass KI Tools gerade die Art verändern, wie wir arbeiten?

INTRO:
Willkommen! Heute schauen wir uns {topic} an – einfach erklärt.

MAIN:
Diese Tools sparen Zeit, reduzieren Fehler und skalieren Prozesse.

OUTRO:
Abonniere für mehr ehrliche Tech-Videos.
"""

timestamp = datetime.now().strftime("%Y%m%d_%H%M")

script_file = SCRIPT_DIR / f"script_{timestamp}.txt"
script_file.write_text(script_text, encoding="utf-8")

output_file = OUTPUT_DIR / f"READY_{timestamp}.txt"
output_file.write_text("Pipeline erfolgreich gestartet", encoding="utf-8")

print("✅ Script generated")
print("✅ Pipeline base OK")
