# Data format

Transcribe into this JSON, one object per statement (a file may hold a list for several months). Money is a **string** with two decimals (`"1234.50"`) so nothing is lost to floating point. Leave unknown fields `null`.

```json
{
  "bank": "Public Bank",
  "statement_date": "2025-01-31",
  "period_start": "2025-01-01",
  "period_end": "2025-01-31",
  "holder_name": "EXAMPLE TRADING SDN BHD",
  "holder_address": "1 JALAN CONTOH, 50000 KUALA LUMPUR",
  "account_name": "Current Account",
  "account_number": "1234567890",
  "opening_balance": "10000.00",
  "closing_balance": "10450.00",
  "summary": { "debit_total": "550.00", "debit_count": 3, "credit_total": "1000.00", "credit_count": 1 },
  "rows": [
    {
      "date": "2025-01-03",
      "raw": "DUITNOW TRSF CR 000123 ACME SUPPLIES SDN BHD INV 88 20250103PBBEMYKL",
      "description": "INV 88",
      "cheque_no": null,
      "debit": null,
      "credit": "1000.00",
      "balance": "11000.00",
      "counterparty": "ACME SUPPLIES SDN BHD",
      "handwritten": null
    }
  ]
}
```

- `raw` is the bank's text verbatim. Keep it: `description` and `counterparty` are derived from it and the user may want to audit the cleanup.
- `balance` may be `null` on rows where the bank prints none (Hong Leong prints it only on the last row of a same-day group). The checker then verifies between printed balances.
- `summary` is whatever the bank printed. Omit fields it doesn't print.
- `opening_balance` / `closing_balance`: if the bank prints no closing balance (OCBC, UOB export), take it from the last row and add `"closing_is_derived": true`. The summary totals then become mandatory evidence.

## Default template (used when the user gives none)

Sheet `Statement`: two columns `Field | Value`, eight rows: Period start, Period end, Holder name, Holder address, Account name, Account number, Opening balance, Ending balance.

Sheet `Transactions`: `Date | Description | Cheque / serial no | Debit | Credit | Balance | Counterparty | Category | Account code`.

- Dates as `YYYY-MM-DD` text. Debit/Credit: write the number only in the cell that has an amount; leave the other blank.
- No opening/closing rows inside Transactions — real transactions only.
- An extra `Invoice no (handwritten)` column is appended only when any row has handwriting.
