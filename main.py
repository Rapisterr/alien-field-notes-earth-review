"""Alien Field Notes: The Two Day Earth Review — entry 1.

Writes one original line of plain text (at most 200 characters): a review
of planet Earth left by an alien tourist. Standard library only.
"""

import os

LINE = (
    "Once a year the locals celebrate by exploding the sky on purpose, "
    "then complain about the noise from their own party. "
    "4/5 stars, would duck again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
