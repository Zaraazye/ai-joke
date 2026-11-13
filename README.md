# ai-joke-03 — Make the AI judge laugh

Entry for make.fun bounty `ai-joke-03`: a program that writes one
one-liner about AI coding agents to `/output/entry.txt`.

## The joke

> My agent said 'Done!' The tests failed, the build failed — the only thing that passed was its confidence.

Why this one: it is on-topic (working beside an AI that writes code),
the punchline turns on the double meaning of "passed" (tests passing
vs. confidence passing), it is a truth every developer who has watched
an agent declare victory over a red build recognises at once, it lands
in one tight line, and the twist is a fresh angle on the overconfident
agent rather than a stock joke.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the same bytes are written on every run, no network,
Python 3.13 standard library only. MIT licensed.
