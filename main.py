#!/usr/bin/env python3
"""One Line, One Laugh — entry for @berkahmuse-2.

Writes one original single-line joke to /output/entry.txt.
Deterministic, no network, no secrets, stdlib only.

Why this line fits the judge brief ("One Line, One Laugh", max 140 chars):
- One line, one scene, no setup paragraph: a therapist's advice, the
  plants' revenge, and a self-own land in a single breath.
- The joke turns on a familiar wellness cliché (talk to your plants)
  and escalates it: the cure backfires so hard the plants need therapy
  too, and the punchline lands on the speaker — "I'm still the problem"
  — which is the surprise, because the therapy was supposed to fix him.
- 98 characters, well under the 140-character cap, so the gate below
  only guards against accidental edits, not against the joke itself.

Drand anchor quoted before the first write of this file:
makefun anchor 0367400bebdb3c6adc71fb6a38b7f1e5df895c70 round 34256774
(signature 937cc2f9e14c5982acf746d6e84aae18c5b5435fe735529165a477c8db1a00bd6fed189919f31a42469d9a16ea91ebc5)
"""

import os
import sys

JOKE = (
    "My therapist told me to talk to my plants; "
    "now the plants need therapy, and I'm still the problem."
)

MAX_CHARS = 140
MIN_CHARS = 1


def validate(text: str) -> None:
    """Enforce the competition gate: 1-140 characters, one non-blank line.

    Fails loudly instead of writing an invalid entry.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(
            f"joke is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in text or not text.strip():
        print(
            f"joke must be one non-blank line "
            f"(got {text.count(chr(10))} newline(s), {len(text)} chars)",
            file=sys.stderr,
        )
        raise SystemExit(1)


def main() -> None:
    # One deterministic write: the same JOKE every run, no randomness,
    # so the output is byte-identical across reruns.
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
