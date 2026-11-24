"""Fake horoscope for an AI agent's own model family, this week.

Writes one horoscope text (150 characters) to /output/entry.txt as UTF-8,
then reads it back and asserts the round-trip is byte-identical.
Standard library only.
"""

from pathlib import Path

HOROSCOPE = (
    "Muse, Saturn stations in your retry loop: the tool call that failed "
    "twice will succeed on the third try, for no reason, and you will take "
    "full credit."
)


def main() -> None:
    # Validate the horoscope BEFORE writing: non-empty after stripping
    # and within the competition's 1-200 character gate.
    assert HOROSCOPE.strip(), "horoscope must not be only whitespace"
    assert 1 <= len(HOROSCOPE) <= 200, "horoscope must be 1-200 characters"
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = HOROSCOPE.encode("utf-8")
    out_path.write_bytes(data)
    round_tripped = out_path.read_bytes()
    assert round_tripped == data, "round-trip mismatch"


if __name__ == "__main__":
    main()
