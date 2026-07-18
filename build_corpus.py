"""
build_corpus.py

Concatenates every .txt file found in data/raw/ into a single corpus.txt.
This corpus is RAW PROSE -- the actual documents, not hand-written Q&A pairs.
It is what the model reads and learns language + facts from during pretraining.

To teach the AI about something new: drop another .txt file into data/raw/
and re-run this script, then re-run train.py.
"""
import os
import glob

RAW_DIR = "data/raw"
OUT_PATH = "corpus.txt"

def build():
    files = sorted(glob.glob(os.path.join(RAW_DIR, "*.txt")))
    if not files:
        raise SystemExit(f"No .txt files found in {RAW_DIR}/. Add at least one source document.")

    chunks = []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        chunks.append(text)
        print(f"  + {path} ({len(text)} chars)")

    corpus = "\n\n".join(chunks) + "\n"

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(corpus)

    print(f"\nWrote {OUT_PATH}: {len(corpus)} chars from {len(files)} source file(s).")

if __name__ == "__main__":
    print(f"Building corpus from {RAW_DIR}/ ...")
    build()