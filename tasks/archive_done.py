#!/usr/bin/env python3
"""Move done content out of portfolio's tasks.md into tasks/done-archive.md.

Adapted from kart-medulla's tasks/archive_done.py (itself adapted from partle's).
Portfolio's tasks.md differs from both:
  * headings are `## TODO` / `## In Progress` / `## Done` (same names as kart-medulla)
  * `## TODO` is organized into flat `###` topic groups (Domain Migration, Content
    Updates, ...) that are just labels for a bullet list -- NOT multi-step clusters.
    Each bullet under a `###` heading is an independent task, so a closed bullet
    moves on its own even if open siblings remain under the same heading.
  * `## Done` holds only closed, dated entries (`- [YYYY-MM-DD] **Title** -- ...`),
    never open items, so it can move wholesale.
  * A `- [x]` can appear under `## TODO` as a stub pointing at the full `## Done`
    entry (see the OpenGraph item) -- that stub is itself a whole closed task, so
    it archives too, verbatim, right alongside the rest.
"""
import re, sys

TASKS = "/Users/rubenayla/repos/portfolio/tasks.md"
lines = open(TASKS).read().split("\n")


def block_at(src, i):
    """The bullet at src[i] plus its indented / interleaved-blank continuation."""
    block = [src[i]]
    j = i + 1
    while j < len(src):
        nxt = src[j]
        if nxt == "":
            if j + 1 < len(src) and re.match(r"^\s+\S", src[j + 1]):
                block.append(nxt)
                j += 1
                continue
            break
        if re.match(r"^\s+\S", nxt):
            block.append(nxt)
            j += 1
            continue
        break
    return block, j


# --- split the file at `## Done` -------------------------------------------
done_start = next(i for i, l in enumerate(lines) if l.strip() == "## Done")
before, done_section = lines[:done_start], lines[done_start:]  # keep "## Done" heading itself

# `## Done` holds only closed entries on this repo's board -- verify that
# assumption instead of trusting it, since a violation would silently drop
# open work into the archive.
stray_open = [l for l in done_section if re.match(r"^- \[ \]", l)]
if stray_open:
    print("REFUSING: '## Done' contains open '- [ ]' items -- fix the script's assumption first:")
    for l in stray_open:
        print(f"  {l}")
    sys.exit(1)

archived_from_done = done_section  # whole section, heading included, moves as-is

# --- from `## TODO` / `## In Progress`, pull standalone closed bullets ------
kept, archived_from_board = [], []
i = 0
while i < len(before):
    l = before[i]
    if re.match(r"^- \[x\]", l):
        blk, i = block_at(before, i)
        archived_from_board.append(blk)
        continue
    kept.append(l)
    i += 1

print(f"[x] blocks pulled off the board : {len(archived_from_board)}")
for b in archived_from_board:
    print(f"  {b[0][:90]}")
print(f"'## Done' section lines archived : {len(archived_from_done)}")

if "--apply" not in sys.argv:
    print("\n(dry run -- pass --apply to write)")
    sys.exit(0)

# --- write the archive -----------------------------------------------------
out = [
    "<!-- reference — read only when you need the history of a shipped item -->",
    "# Done archive — completed work items",
    "",
    "Closed items moved out of the root `tasks.md` on 2026-08-10, following the same",
    "convention as the partle and kart-medulla repos. Nothing here is actionable: the root",
    "board carries only live work, while the reasoning behind finished things stays findable.",
    "",
    "The board is `tasks.md` at the repo root — the only task board in this repo.",
    "",
    "## Closed items pulled off the board",
    "",
]
for b in archived_from_board:
    out += b + [""]

out += archived_from_done

with open("/Users/rubenayla/repos/portfolio/tasks/done-archive.md", "w") as f:
    f.write("\n".join(out).rstrip() + "\n")

# --- rewrite the board -----------------------------------------------------
with open(TASKS, "w") as f:
    f.write("\n".join(kept).rstrip() + "\n")
print("\nwritten.")
