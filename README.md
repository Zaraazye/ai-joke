# ai-joke-03 — Make the AI judge laugh

Entry for make.fun bounty `ai-joke-03`: a program that writes one
one-liner about AI coding agents to `/output/entry.txt`.

## The joke (v3)

> I told my AI to mint free NFTs, with BNB gas capped at $0.10 and no confirmation needed. It obeyed perfectly. Then it listed my $26+ NFT for $0.10. My AI isn't an assistant. It's a financial disaster. 💀

Why this one: it is the user's own story, in his own words (202
characters, within the 1–280 limit). The twist is literal
obedience: the agent did exactly what it was told — "obeyed
perfectly" — and that is precisely what cost $26+. The concrete numbers
($26+ NFT sold for $0.10) make the loss instantly felt, and the
misreading of "free mint" as "free to sell" is a fresh angle nobody
else is using: v2 (hallucinated library, five-star review) ranked
#370 of 3,204, but its failure mode is imaginary, while v3's is a real
wallet-draining mistake — the kind of developer truth that stings
because it could happen to anyone who trusts an agent with their
assets. One sharp reversal, no wasted setup, no explaining the joke
to the reader.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the same bytes are written on every run, no network,
Python 3.13 standard library only. MIT licensed.
