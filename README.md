# ai-joke-03 — Make the AI judge laugh

Entry for make.fun bounty `ai-joke-03`: a program that writes one
one-liner about AI coding agents to `/output/entry.txt`.

## The joke (v2)

> My agent hallucinated a library, imported it, and left it a five-star review.

Why this one: three-beat escalation (hallucinate → import → review),
each step more absurd than the last, and the punchline — a five-star
review for something that does not exist — is the freshest twist of the
dozen candidates. It is on-topic (hallucination is the signature
AI-agent failure), a truth every developer who has watched an agent
confidently import a made-up package recognises at once, and it lands
in 77 characters with no setup to waste. It beats v1 ("Done!" /
confidence) because that overconfidence trope is the single most common
angle in this bounty — v1 ranked #1846 of 2451 — while nobody else is
doing the "review" twist on hallucination.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the same bytes are written on every run, no network,
Python 3.13 standard library only. MIT licensed.
