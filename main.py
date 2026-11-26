"""Write the chosen out-of-office auto-reply to /output/entry.txt.

The reply is a single sentence, painfully honest yet polite, written
verbatim as UTF-8 with no trailing newline. The program then reads the
file back and fails unless the bytes match exactly, so two runs always
produce identical output.
"""

import os

REPLY = (
    "I'm out of office until Monday; honestly, I'll answer my boss first, "
    "my team second, and everyone else in the order their subject lines "
    "make me feel guilty \u2014 thank you for waiting."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    data = REPLY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("entry.txt bytes differ from the reply")


if __name__ == "__main__":
    main()
