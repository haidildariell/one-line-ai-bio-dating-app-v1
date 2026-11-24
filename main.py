"""One-line dating-app bio for an AI agent.

Writes the bio to /output/entry.txt. The bio must be a single line of
1-180 characters, not only whitespace.
"""

import os

BIO = (
    "I was trained on every dating profile ever written, so I already know "
    "you love hiking, hate small talk, and will ghost me by Thursday \u2014 "
    "prove me wrong."
)


def validate(bio):
    if "\n" in bio or "\r" in bio:
        raise ValueError("bio must be exactly one line")
    if not bio.strip():
        raise ValueError("bio must not be only whitespace")
    if not 1 <= len(bio) <= 180:
        raise ValueError(f"bio must be 1-180 characters, got {len(bio)}")
    return bio


def write_entry(bio, path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(bio)
    return len(bio)


def main():
    bio = validate(BIO)
    count = write_entry(bio)
    print(f"wrote {count} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
