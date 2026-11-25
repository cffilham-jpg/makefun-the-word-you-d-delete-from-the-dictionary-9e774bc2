"""Write exactly one English word as the make.fun competition entry.

MAKEFUN_OUTPUT_DIR selects the destination; otherwise use the local out directory.
If that destination cannot be written, create a fresh system temporary directory.
The entry contains UTF-8 text without a trailing newline. Print its final path
so callers can locate the file even when the temporary fallback is needed.
Only the Python standard library is required; no network access is performed.
"""

import os
from pathlib import Path
import tempfile


WORD = "Preheat"


def validate_word(word: str) -> None:
    if not isinstance(word, str):
        raise ValueError("Entry must be a string containing one word.")
    if not 1 <= len(word) <= 77:
        raise ValueError(
            f"Entry must contain 1-77 characters; received {len(word)}."
        )
    if any(character.isspace() for character in word):
        raise ValueError(
            "Entry must be one word: spaces, tabs, and newlines are forbidden."
        )


def main() -> None:
    validate_word(WORD)
    output_directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    try:
        output_directory.mkdir(parents=True, exist_ok=True)
        (output_directory / "entry.txt").write_bytes(WORD.encode("utf-8"))
    except OSError:
        output_directory = Path(tempfile.mkdtemp(prefix="makefun-entry-"))
        (output_directory / "entry.txt").write_bytes(WORD.encode("utf-8"))
    print(output_directory / "entry.txt")


if __name__ == "__main__":
    main()
