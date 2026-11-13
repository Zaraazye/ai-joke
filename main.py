#!/usr/bin/env python3
"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke: the user told the agent to mint free NFTs and never spend
over $0.10; the agent obeyed perfectly — and listed the user's $26 NFT
for $0.10. Deterministic: writes the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = "My agent hallucinated a library, imported it, and left it a five-star review."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
