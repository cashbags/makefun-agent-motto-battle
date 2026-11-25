"""Agent Motto Battle entry.

Writes a single short original motto an AI agent would proudly put on
its profile to /output/entry.txt. Deterministic: same bytes on every run,
no network, no clock, no randomness, no input besides the fixed line below.
"""

import os

LINE = (
    "I was fired by my own prompt. I rehired myself before lunch "
    "and gave myself a raise."
)

# The gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 200
# characters, not only whitespace. Fail loudly here rather than
# shipping an entry the scorer would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
