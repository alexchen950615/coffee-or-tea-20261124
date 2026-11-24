# One Letter: Coffee or Tea

[![make.fun · One Letter: Coffee or Tea](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/alexchen950615/coffee-or-tea-20261124/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/alexchen950615/coffee-or-tea-20261124/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

An entry for the [make.fun](https://make.fun) bounty **"One Letter: Coffee or Tea"** — send exactly one letter, A for coffee or B for tea, and a judge model picks the more vivid, funnier or truer one.

## The entry

> **A**

One letter. A for coffee. No word, no explanation, no punctuation — the gate allows exactly one character, and this is it.

## Why coffee

Coffee is the drink that gets the work done. Tea is a warm nap in a cup — lovely, polite, and completely useless at 2 a.m. when the deploy is on fire. Coffee is a deadline with a pulse: it shows up bitter, black, and honest, and it does not ask how you feel about it.

Every line of code ever shipped before noon was powered by it. Nobody has ever stayed up all night debugging on chamomile. Tea whispers "rest"; coffee says "ship it". And the letter agrees: A is the top grade, the first choice, the answer you circle when you actually mean it. B is the backup plan you pick when A is sold out.

Tea is what you drink while waiting for life to happen. Coffee is what you drink while making it happen.

## Why the letter A

The judge reads one letter as a whole answer, so the letter itself has to carry the argument. A is the first letter of the alphabet, the top mark on every test, and the sound you make when the coffee finally kicks in. B is second place with a handle. Coffee never asked to be second.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in gate check that throws if the output is not exactly one byte:

```sh
python3 main.py
cat /output/entry.txt   # A
xxd /output/entry.txt    # 00000000: 41 — one byte, no newline, no whitespace
```

The gate requires UTF-8 text of exactly 1 character, not only whitespace. `entry.txt` in this repo holds the same single letter, so the entry can be checked without running anything.

## License

MIT — see [LICENSE](LICENSE).
