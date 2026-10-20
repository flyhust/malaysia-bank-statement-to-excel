# Public Bank Malaysia (PBB / Public Islamic) — printed statement

- One statement per month, usually 1–3 pages. Page 1 has a Summary: closing balance, debit total + count, credit total + count. That is the answer key.
- Dates print `dd/mm`; the year comes from the Statement Date.
- **Only the first row of a day prints the date.** Following rows inherit it.
- Rows begin after `Balance From Last Statement` and end at `Closing Balance In This Statement`.
- **Page breaks**: `Balance C/F` at the foot, `Balance B/F` at the next head. B/F is not an opening. The previous page's last reference number (`2025…PBBEMYKL…`) sometimes lands *under* the next page's B/F — it belongs to that last row, it is not a new transaction.
- A row is up to ~3 lines: type + serial + amount + balance; payer/payee name; customer note; often a trailing bank reference.
- `GST DR` / `SST DR` rows at 0.00 are counted in the debit count.
- Some PDFs have column positions that separate Debit/Credit, others flatten them to one amount. Take direction from the balance movement in either case.
- Months with no activity still have B/F and C/F lines; produce a file with headers only.

# Public Bank Malaysia — PBBe internet-banking export ("Account Summary - Savings / Current Account Details")

A different document: no letterhead, no B/F. A record opens on a full `dd/mm/yyyy` date and closes on the line that **ends with `amount  balance`**; everything between is narrative, wrapped arbitrarily. Debit/Credit are flattened to one amount → direction from the balance movement.
