import os

TEXT = "Synchronized Napping: four athletes nap in perfect unison; snoring costs a point, sleep-talking is a foul, and the gold goes to the team that dreams in formation."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
