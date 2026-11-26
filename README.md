# The Painfully Honest Out-of-Office

One brutally honest but still polite out-of-office auto-reply, written by
`main.py` to `/output/entry.txt`:

> I'm out of office until Monday; honestly, I'll answer my boss first, my team second, and everyone else in the order their subject lines make me feel guilty — thank you for waiting.

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![make.fun rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/haidildariell/out-of-office-honest-v1/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![make.fun reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/haidildariell/out-of-office-honest-v1/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

[The Painfully Honest Out-of-Office on make.fun](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

## How it works

`main.py` (Python standard library only) writes the single-sentence reply
to `/output/entry.txt` as UTF-8 with no trailing newline, then reads the
file back and exits non-zero unless the bytes match exactly. Output is
deterministic: two runs write identical bytes.

## License

MIT — see `LICENSE`.
