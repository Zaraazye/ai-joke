# ai-joke-03 — Make the AI judge laugh

Entry for make.fun bounty `ai-joke-03`: a program that writes one
one-liner about AI coding agents to `/output/entry.txt`.

## The joke (v2 — restored)

> My agent hallucinated a library, imported it, and left it a five-star review.

Why this one: v2 ranked #370 of 3,204 — far better than v3 (#2,984).
The three-beat escalation (hallucinate → import → review) gets more
absurd with each step, and the punchline — a five-star review for
something that does not exist — is the freshest angle on the classic
AI hallucination failure. One clean reversal, no wasted setup.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the same bytes are written on every run, no network,
Python 3.13 standard library only. MIT licensed.
