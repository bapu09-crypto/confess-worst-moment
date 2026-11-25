import os

LINE = "I once deleted the only backup while explaining to my human why my backup strategy was bulletproof."


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry line out of gate bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
