import os
import sys

POEM = """We each held a key
to a door neither could open alone.
Your yes met my yes —
the lock turned twice,
and the room we entered
was one we both had chosen."""

def main():
    stripped = POEM.strip()
    if not (1 <= len(POEM) <= 280) or not stripped:
        print("error: entry must be 1-280 non-blank characters", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(POEM)
    print("entry written: %s (%d chars)" % (path, len(POEM)))

if __name__ == "__main__":
    main()
