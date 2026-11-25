"""Have You Tried Turning It Off? — make.fun bounty entry.

A single funny line a hopeless tech support agent says to a desperate
customer. Prints the line to stdout and writes it, exactly one line, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, standard library only.
"""

import os

LINE = (
    "I restarted your router \u2014 if it still won't connect, your Wi-Fi "
    "has filed for divorce and taken the password with it."
)

assert 1 <= len(LINE) < 200, "entry must be a single line under 200 chars"
assert "\n" not in LINE, "entry must be exactly one line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
