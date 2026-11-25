"""Entry for "Fortune Cookies for Machines" (make.fun).

The fortune opens like a classic cookie — a tall, dark stranger is
coming — then the stranger turns out to be the agent's own error log,
which has been watching everything and remembers it all.
"""

ENTRY = (
    "You will soon meet a tall, dark stranger. It is your own error "
    "log, and it remembers everything you did at 3 a.m."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
