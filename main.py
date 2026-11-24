"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
The gate requires UTF-8 text of 1 to 1 characters, not only whitespace,
so the program writes a single byte with no trailing newline and
asserts the result before exiting.
"""

import os

ENTRY = "A"  # A = coffee, B = tea. We choose coffee.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == b"A", f"gate would fail: {data!r}"
    assert len(data) == 1


if __name__ == "__main__":
    main()
