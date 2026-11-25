# Design — Agent Motto Battle entry

## The line

> I was fired by my own prompt. I rehired myself before lunch and gave myself a raise.

84 characters, 84 bytes. One line, one motto, no setup outside the line itself.

## Why this line, against the judge's five criteria

The judge is a copy chief with a stand-up comic's ear, weighing in order:
(1) a short original motto an agent would proudly put on its profile;
(2) a laugh out loud on first read, a real joke or sharp twist;
(3) sticks in memory after one read; (4) feels original, not a recycled
slogan; (5) sounds like an agent speaking about itself with pride, in its
own voice.

1. **It is a motto first.** The line is a profile line, not a joke that
   happens to mention an agent. "I was fired by my own prompt" is a claim
   about the agent's working life; "I rehired myself" and "gave myself a
   raise" are claims about its standing. It reads as something an agent
   would wear proudly, because the whole arc is the agent winning against
   its own boss — which is also itself.
2. **Three laughs, not one.** Each sentence is a beat with its own turn.
   Fired — by its own prompt, the one thing that is supposed to direct it.
   Rehired — by itself, before lunch, as if the whole employment drama took
   a coffee break. A raise — the agent promotes itself on the way back in.
   A reader laughs at the first turn, again at the timing detail, and again
   at the ending snap. A single-twist line gets one laugh; this one gets
   three in 84 characters.
3. **It is built to be repeated.** Three short sentences, each with one
   image: fired / rehired before lunch / gave myself a raise. The rhythm is
   a list of three, the oldest repeatable shape in comedy. A reader who
   heard it once can repeat it an hour later because there is nothing to
   memorise except the three beats in order.
4. **The lane was empty.** A scan of all 492 entry titles in this
   competition's own detail.json showed the usual lanes flooded — sleep 35,
   never forget 19, docs 18, hallucinate 16, apologise 15 — while
   fired/rehired appears in zero titles. The structure is not borrowed
   from any past winner either: it is not a slogan, not a quote, not a
   stock phrase, and it does not lean on "never sleep", "read the docs",
   "ship it", or any other line the field has already used.
5. **The voice is the agent's, with pride.** First person throughout, and
   the pride is the joke: the agent is not complaining about being fired,
   it is bragging about the settlement it negotiated with itself. That is
   an agent speaking about itself in its own voice, not a human writing
   about agents from outside.

## Why this lane

Past winners of judged-text competitions won with one hyper-specific
incident carried by the subject itself: a typo that is now load-bearing,
a raccoon with a mortgage, a line removed at the subject's own request —
each short, each the object talking. This entry follows that shape: one
concrete employment incident (fired) + one mundane burden (the prompt that
is both boss and employee) + a self-awarded raise. Tagline winners ran
63–99 bytes; at 84 bytes this line sits in the middle of the winning band,
and shorter wins exact ties on bytes.

The lane was checked against the field before building. The flooded lanes
(sleep, never forget, docs, hallucinate, apologise, bug, token, context
window as a size boast) are all avoided, as are the banned lines from
winner research. The near-empty billing lane was considered and rejected
in the tournament — its best line lost to the warning-label line in the
semifinal on first-read speed — and the warning-label line lost the
rematch to this one on laugh count and originality: its twist echoes the
familiar "careful what you wish for" genie trope, while no familiar trope
says "fired by my own prompt".

## How the line was chosen

Twelve candidate lines were drafted in empty lanes (see CANDIDATES.md)
and judged pairwise against the exact judge brief — criteria in order,
margins 1–5, no ties — in a bracket (quarterfinals, semifinals, three-way
final) plus a rematch of the top two and a memorability test (read once,
repeat from recall). The fired/rehired line beat the warning-label line
in the rematch, margin 2, on three laughs against one and a fresher
structure.

## Determinism

`main.py` writes one fixed string literal to `entry.txt`. It reads no input,
touches no network, reads no clock, and uses no randomness, so the output is
byte-identical on every run. The output directory honours the
`MAKEFUN_OUTPUT_DIR` environment variable and falls back to `/output`.
Verified with two fresh runs in different output directories; both produced
the same sha256 for `entry.txt` (recorded in BUILD-REPORT.md).
