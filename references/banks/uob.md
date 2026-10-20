# UOB Malaysia — printed statement ("Aktiviti Akaun Anda")

- Bilingual letterhead; `BALANCE B/F` and `BALANCE C/F` bracket each page; account summary on the final page.
- A row opens with **two dates** (transaction, value) and ends with amount + running balance:
  `08 FEB 08 FEB DuitNow/Instant Trf 1,250.00 8,430.10`, then narrative (`SALARY-JAN`), then bank code + counterparty.
- Every row prints a balance → direction from the balance delta (safer than column position on a skewed scan).
- The bilingual legal footer ends the table; nothing continues past it.

# UOB Malaysia — "Account Activities" portal export

Not a statement: no letterhead, no B/F/C/F, no closing balance — just a record count, rows, and a pair of totals.

```
02/11/2025                 <- statement date alone on its line: opens a record
01/11/2025 01:36:53 PM     <- transaction date/time
DuitNow/Instant Trf        <- type
Fund transfer ...          <- narrative, counterparty, packed fields
500.00   0.00   9,876.50  <- deposit, withdrawal, balance
```

Opening and closing are both derived from the rows, so the export's own totals and record count are the only independent evidence — they must match.
