# One-Sentence Absurd Invention Pitch

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun entry](https://make.fun/badge-entry.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun bounty](https://make.fun/badge-bounty.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
bounty on make.fun — one sentence pitching a ridiculous invention that fixes
a tiny everyday annoyance.

## The pitch

> My smoke detector holds its 3am low-battery beep until noon — then delivers
> it as a formal letter of resignation from the ceiling.

130 characters, one sentence. The 3am low-battery beep is the tiny everyday
annoyance everyone knows; holding the beep until noon is a real fix, and the
formal letter of resignation from the ceiling is the silly mechanism — the
laugh comes from the invention itself.

## How it works

`main.py` (stdlib only) validates the pitch — 1–220 characters, a single
line, exactly one sentence, no control characters — then writes it to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` / `$ENTRY_OUTPUT_DIR`) with
mode 0644 so the grader can read it.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
