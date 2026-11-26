"""Painfully honest out-of-office reply.

Writes a single-sentence out-of-office reply to /output/entry.txt as
UTF-8 with no trailing newline, then reads the file back and fails if
the bytes differ. Deterministic: every run writes identical bytes.
"""

import hashlib
import os
import sys

REPLY = "I'm out of office until Monday; honestly, I'll answer my boss first, my team second, and everyone else in the order their subject lines make me feel guilty — thank you for waiting."

OUTPUT_PATH = "/output/entry.txt"


def validate_reply(reply):
    """Check the reply is 1-200 characters and exactly one sentence."""
    if not (1 <= len(reply) <= 200):
        print(f"error: reply length {len(reply)} outside 1-200", file=sys.stderr)
        return False
    if reply.count(".") != 1 or not reply.endswith("."):
        print("error: reply must be exactly one sentence", file=sys.stderr)
        return False
    return True


def write_entry(path, data):
    """Write bytes to path, creating parent directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def verify_entry(path, expected):
    """Read path back and fail unless its bytes match expected exactly."""
    with open(path, "rb") as f:
        back = f.read()
    if back != expected:
        print("error: read-back bytes differ", file=sys.stderr)
        return False
    return True


def main():
    if not validate_reply(REPLY):
        return 1
    data = REPLY.encode("utf-8")
    write_entry(OUTPUT_PATH, data)
    if not verify_entry(OUTPUT_PATH, data):
        return 1
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
