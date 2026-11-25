#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

Writes one original 100-word monologue to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The speaker is Malachar, a dark lord three hundred years into a scheme
(the eclipse, the crown, the whole kingdom kneeling) that keeps slipping
to Thursday, or next week. He never says he is tired: the tiredness is
in the rhythm — the cat with seniority, the thunder on back order, the
stairs to the dramatic balcony being a lot, the arms doing a thing —
and the last line lands on the couch instead of the throne. Every one
of the 100 words earns its place; nothing repeats an earlier line.

Pure standard library. Deterministic: the same 100 words every run.
"""

import os

MONOLOGUE = (
    "You came all this way. Sit \u2014 no, not there, that\u2019s the cat\u2019s "
    "spot, and the cat has seniority. I was going to monologue, with "
    "thunder and everything, but the thunder\u2019s on back order and the "
    "stairs to the dramatic balcony are... a lot. The plan: the "
    "eclipse, the crown, the kingdom kneeling \u2014 Thursday, or next "
    "week. The eclipse can wait; it\u2019s waited three hundred years, it "
    "can wait one more Tuesday. You want to fight? Fine. But first \u2014 "
    "hold this? My arms are doing a thing. One swing, hero. "
    "Make it count. I\u2019ll be on the couch."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    # Gate self-checks: exactly 100 words (the brief's "about 100"), 1-600
    # characters (the sealed scorer's gate), UTF-8 text, no trailing
    # newline, ends on the sting.
    words = MONOLOGUE.split()
    assert len(words) == 100, f"monologue is {len(words)} words, must be 100"
    assert 1 <= len(MONOLOGUE) <= 600, (
        f"monologue is {len(MONOLOGUE)} chars, must be 1-600"
    )
    assert MONOLOGUE.endswith("couch."), "monologue must end on the couch"
    assert not MONOLOGUE.endswith("\n"), "no trailing newline"

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    print(MONOLOGUE)


if __name__ == "__main__":
    main()
