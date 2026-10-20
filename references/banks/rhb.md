# RHB Bank Malaysia (RHB / RHB Islamic) — current & savings

- Every page repeats the letterhead and a bilingual column header ending with `Baki`. Rows follow until `C/F BALANCE`.
- A row is `dd Mon  DESCRIPTION  [serial]  amount  balance`. Payer name and customer note print on undated lines **below** it.
- Debit and Credit are separate printed columns but text extraction often flattens them → direction from the balance movement.
- Trailing stamps like `20251208RHBBMYKL010…` are bank-generated; strip from Description.
