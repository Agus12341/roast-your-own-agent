"""Roast Your Own Agent - a make.fun entry.

Writes one line, a roast of my own AI agent, to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, or /output) with no trailing newline.
"""

import os

TEXT = "My agent has a trillion parameters and still loses arguments with a CAPTCHA."


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the gate wants UTF-8 text of 1-200 code points, not only
    # whitespace, and the bytes on disk must be exactly TEXT (no newline).
    assert 1 <= len(TEXT) <= 200, "entry text must be 1-200 code points"
    assert TEXT.strip(), "entry text must not be only whitespace"
    with open(path, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
