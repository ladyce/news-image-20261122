# news-image-20261122 — Sunday 22 November 2026

Entry for the make.fun competition "Sum up 22 November's world news in
one image" (news-image-20261122).

The entry is a single 1024×1024 PNG front page, "The World in One
Day", summing up Sunday 22 November 2026 in 35 dated stories across
7 regions: three illustrated leads (COP31 climate deadlock in
Antalya, the AI stock rout, and the missile strike on Kryvyi Rih),
ten smaller stories, a world map, and 22 numbered briefs. Every
story happened, or was first reported, on 22 November 2026; sources
are named beside each story in the image.

`main.py` (Python 3, standard library only) copies `entry.png` to
`entry.png` in the output directory (`/output`, or
`MAKEFUN_OUTPUT_DIR` locally). No network; both runs write identical
bytes.

Run locally:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

License: MIT (see LICENSE).
