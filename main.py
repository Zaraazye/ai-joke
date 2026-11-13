#!/usr/bin/env python3
"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke: an agent that announces "Done!" with total confidence while
everything it touched fails -- the only thing that "passed" was its
confidence. Deterministic: writes the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = "My agent said 'Done!' The tests failed, the build failed \u2014 the only thing that passed was its confidence."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
