---
name: malaysia-bank-statement-to-excel
description: Convert bank statements (PDF, scanned or text-native, one or many months) into an Excel workbook that follows the user's own template, with every row proven by the balance chain and the bank's printed totals. Use when the user asks to convert, transcribe or extract a bank statement / 对账单 / penyata bank into Excel or a template, to reconcile statement rows, or to merge a year of monthly statements into one file. Built for MALAYSIAN bank statements (RM): layout notes for Public Bank, Maybank, CIMB, RHB, Hong Leong, OCBC Malaysia and UOB Malaysia, plus a generic method for any other bank.
---

# Malaysian bank statement → template-shaped Excel

Scope: statements issued by banks in **Malaysia** (amounts in RM, Malay/English/Chinese headers, DuitNow, JomPAY, IBG, GIRO). Every note in `references/banks/` is for the Malaysian edition of that bank; the same bank in Singapore or Indonesia prints a different layout and should be treated as a bank without notes.

## Principles

1. **The template rules.** If the user gives an xlsx template, load it and fill it. Do not redesign it.
2. **Amounts come from the page; trust comes from arithmetic.** Never judge a digit by eye. The balance chain decides whether a transcription is trustworthy.
3. **The customer's own words are untouched.** Strip what the bank generated; keep what the account holder typed, exactly as typed.
4. **Every judgement call is reported.** Wherever the template is silent and you chose, say so at delivery.

## Order of work

1. **Read the template first** (if any). Note sheet names, headers, font, whether dates are text or real dates, number formats, which columns are empty. If there is no template, use the default one (`scripts/fill_template.py` creates it; layout in [references/data-format.md](references/data-format.md)).
2. **Identify the bank and the document type**, then read only that bank's notes in `references/banks/`. A printed statement and an internet-banking export from the same bank are different documents. No notes for this bank? Use [references/banks/_generic.md](references/banks/_generic.md).
3. **Transcribe page by page** into the JSON shape in [references/data-format.md](references/data-format.md): date, type, raw narrative, reference, debit, credit, printed balance, handwritten notes. Also capture the statement's own summary (opening, closing, totals, counts) if printed.
4. **Run the checks**: `python scripts/verify.py statement.json`. If it fails, go back to the page image. Never "help" a number pass.
5. **Clean Description and Counterparty** per [references/cleanup.md](references/cleanup.md).
6. **Fill and save**: `python scripts/fill_template.py statement.json out.xlsx [--template tpl.xlsx]`. The script reads the saved file back and re-runs the checks, so what was written is what was verified.
7. **Deliver** (see below).

If an MCP tool or local parser for statements is available (for example a `convert_statement` tool), prefer it for text-native PDFs and still run `verify.py` on its output. Only transcribe by vision when no parser handles the layout.

## Checks (all must pass before delivery)

- Per row: `previous balance − debit + credit = printed balance`, to the cent. Where the bank prints a balance only on some rows, check between printed anchors.
- Per statement: `opening + Σcredit − Σdebit = closing`.
- Per statement: debit total, credit total, debit count, credit count equal the printed summary (when printed).
- Across statements: last month's closing = this month's opening.
- **Direction may be derived from the balance movement. Amount must never be.** An amount computed from the balance delta makes the chain check itself, and a misread digit sails through.
- Report honestly. If you checked by script, say "transcribed, then checked by script: passed". Never claim a bank-parser or third-party validation you did not run.

## Universal layout traps

- **Carried-forward lines are not openings.** `Balance B/F`, `C/F`, `BAKI DIBAWA KE HADAPAN` repeat on every page. The opening is the first page's "balance from last statement" only.
- **Never close a row at a page edge.** Narrative continues on the next page, often after the repeated header or the B/F line. A reference number appearing right under the next page's B/F belongs to the previous page's last row.
- **Dates printed only when they change.** Blank-date rows inherit the date above.
- **Year from the statement date.** Rows print `dd/mm` or `dd Mon`; a December–January statement spans two years.
- **Zero-amount rows count.** `GST DR`, `SST DR` at 0.00 are counted in the bank's debit count. Dropping them breaks the count check.
- **Empty months still get a file**: summary filled, transactions sheet with headers only.

## Handwriting on scans

Handwritten marks (e.g. `INV-1234`) are neither bank- nor customer-typed, so they never go into Description. Put them in an extra right-most column `Invoice no (handwritten)` and tell the user it is outside the template. Crossed-out-and-rewritten: take the rewrite and name it. Illegible: give the most likely reading and ask the user to confirm.

## Delivery

- Follow the template's file granularity (one file per month → `JAN_2025.xlsx` … `DEC_2025.xlsx`). If the user asks for everything combined: one file, opening = first month's opening, closing = last month's closing, period = first to last day, rows in date order.
- Fields the template gives no example for (period dates, account name …): fill them and say where the value came from.
- Columns that are empty in the template (Category, Account code …) stay empty unless the user asks.
- Write the delivery note **in the user's language**: result first, then the list of judgement calls to confirm. Do not narrate your steps.

## Privacy

Statements hold real account numbers, balances and names. Process locally where possible. Anything you write into examples, tests, issues, screenshots or this skill's references must be fictional. Do not echo full account numbers in chat unless the user asks.
