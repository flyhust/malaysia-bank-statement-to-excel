# Any bank without notes

All notes in this folder are for **Malaysian banks** (statements issued in Malaysia, amounts in RM). The same bank in another country (e.g. OCBC Singapore, UOB Singapore, CIMB Indonesia) prints a different layout — treat it as a bank without notes.

Work out these five things from the first two pages before transcribing. Write them down; they become this bank's notes file (please contribute it back).

1. **Where the table starts and ends on each page.** The last line of the repeated column header; the footer/letterhead line after which no row continues. (Maybank prints its letterhead at the *bottom*.)
2. **What opens a row.** A date (`dd/mm`, `dd/mm/yyyy`, `dd Mon`, `dd MON yyyy`), a date pair (transaction + value date), or a statement-date line on its own (portal exports).
3. **Where the amount sits.** Same line as the date, or the last line of the block. Separate Debit/Credit columns, or one column with a sign / `+` / `DR` suffix.
4. **How often a balance prints.** Every row (best: row-by-row check), only at group ends (check between anchors), or never (summary totals become mandatory).
5. **What independent totals the bank prints.** Closing balance, debit/credit totals, counts. These are your answer key.

Then:
- Direction: from the balance delta when balances print; otherwise from the column or sign.
- Narrative lines under the amount line belong to that row until the next row opener, *including across page breaks*.
- Overdrawn balances may print `DR` or with a minus; carry the sign into the JSON (`"-120.00"`).
