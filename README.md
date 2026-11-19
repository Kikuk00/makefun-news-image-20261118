# One image of 18 November 2026 — `news-image-20261118`

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Kikuk00/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Kikuk00/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper-front-page infographic summing up the world's news of
Wednesday 18 November 2026 in one image:
https://make.fun/bounty/news-image-20261118

## The six stories

1. **GULF STRIKES** — Iran fired drones at US-linked bases in Kuwait
   (Ali Al Salem Air Base) and Bahrain after US aircraft struck an
   Iranian missile site on Qeshm Island; Bahrain said it intercepted
   several attacks before dawn.
2. **KERCH BRIDGE FALLS** — Ukraine struck the Kerch Bridge to Crimea
   a second day; its road arch collapsed into the strait. Russia hit
   back at bridges in Kyiv.
3. **SHENZHEN SUMMIT** — Xi Jinping and Vladimir Putin met at APEC in
   Shenzhen, denouncing protectionism and Western sanctions, ahead of a
   first-ever trilateral with Donald Trump on Thursday 19 November.
   Trump was in Manila, where the Quad met at leader level for the
   first time in over two years.
4. **US SENATE FLIPS** — Democrat Mary Peltola won the Alaska Senate
   seat; Democrats take a 56–44 Senate majority.
5. **ISRAEL'S NEW SPEAKER** — Israel's parliament elected Matan Kahana
   as Knesset speaker, a win for prime minister-elect Gadi Eisenkot's
   party and a setback for Netanyahu. Trump's Board of Peace faulted
   Israel and Hamas over Gaza ceasefire commitments.
6. **EBOLA TOPS 11,000** — Ebola in DR Congo passed 11,000 cases; the
   United States lost its measles-free status after 26 years.

The image is drawn entirely by code (flat vector shapes, panels and
text) — no photos, no copied artwork.

## How it works

One file, `main.py` (Python 3.13, standard library only, no network).
It copies the `entry.png` shipped in this repository to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte, so
both runs of the program write identical output.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024x1024 PNG, under 1 MiB).

## Files

- `main.py` — the entry (repository root file)
- `entry.png` — the image: "THE WORLD TODAY — WEDNESDAY 18 NOVEMBER 2026"
- `LICENSE` — MIT
