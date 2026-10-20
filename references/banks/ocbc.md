# OCBC Bank Malaysia — current account

- A row is one line with the date **embedded**: `DUITNOW(INST TRF) DR 02 APR 2026   5,210.40 /IB   120.00`.
- In extracted text the **balance comes BEFORE the amount** (the withdrawal/deposit columns sit to the right of the balance).
- Counterparty, `DESC:` and `REF:` lines follow underneath. `DESC:` is usually the customer's note → Description.
- **No closing balance is printed** — only a TRANSACTION SUMMARY with counts and totals. Closing = last row's balance (`closing_is_derived: true`), which makes the summary check mandatory.
