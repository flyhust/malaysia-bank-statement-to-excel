# Hong Leong Bank Malaysia (Pay&Save, Current Account, CA-i)

- Rows open with `dd-mm-yyyy`.
- **The balance prints only on the LAST row of a group**, not on every row. Leave `balance` null on the others; the checker verifies between printed balances.
- Deposit and Withdrawal are separate columns — direction from which column the amount sits in.
- Page footer looks like `<account number>_<section> <page>`. On some pages it is **run onto the end of the last transaction line**, where it can hide that line's amount. Watch for a row with no amount right before a footer.
- The closing tally may print `.00` with no leading digit on a zero-activity statement.
