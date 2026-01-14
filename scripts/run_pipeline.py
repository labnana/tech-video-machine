import os
import subprocess

INPUTS_DIR = "inputs"
OUTPUTS_DIR = "outputs"

def read_topic(topic_path):
    data = {}
    with open(topic_path, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                data[k.strip()] = v.strip()
            else:
                data["TOPIC"] = line.strip()
    return data

def run():
    print("🚀 Tech Video Machine Pipeline Started")

    for topic_folder in sorted(os.listdir(INPUTS_DIR)):
        topic_dir = os.path.join(INPUTS_DIR, topic_folder)
        topic_file = os.path.join(topic_dir, "topic.txt")

        if not os.path.isfile(topic_file):
            continue

        print(f"\n📄 Processing {topic_folder}")
        topic = read_topic(topic_file)

        video_type = topic.get("TYPE", "SHORT").upper()
        language = topic.get("LANG", "DE")

        # 1️⃣ Generate Voice
        print("🔊 Generating voice...")
        subprocess.run(
            ["python", "scripts/generate_voice.py"],
            check=True
        )

        # 2️⃣ Build Video
        if video_type == "SHORT":
            print("🎬 Building SHORT video")
            subprocess.run(
                ["bash", "scripts/build_short_video.sh"],
                check=True
            )
        else:
            print("🎞️ Building LONG video")
            subprocess.run(
                ["bash", "scripts/build_long_video.sh"],
                check=True
            )

    print("\n✅ Pipeline completed successfully")

if __name__ == "__main__":
    run()
