from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "output/thumbnails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Thumbnail size
WIDTH, HEIGHT = 1280, 720

# Background
bg = Image.new("RGB", (WIDTH, HEIGHT), (15, 23, 42))
draw = ImageDraw.Draw(bg)

# Title text
TITLE = "KI TOOLS\nDIE DICH SCHNELLER MACHEN"

# Font (fallback safe)
try:
    font = ImageFont.truetype("arialbd.ttf", 90)
except:
    font = ImageFont.load_default()

# Center text
text_w, text_h = draw.multiline_textsize(TITLE, font=font)
x = (WIDTH - text_w) / 2
y = (HEIGHT - text_h) / 2

# Glow effect
for i in range(5):
    draw.multiline_text(
        (x-2+i, y-2+i),
        TITLE,
        font=font,
        fill=(56, 189, 248)
    )

# Main text
draw.multiline_text(
    (x, y),
    TITLE,
    font=font,
    fill=(255,255,255),
    align="center"
)

# Save
output_path = f"{OUTPUT_DIR}/thumbnail_tech.png"
bg.save(output_path)

print("✅ THUMBNAIL READY:", output_path)
