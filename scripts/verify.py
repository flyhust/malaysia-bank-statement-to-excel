#!/usr/bin/env python3
"""Check a transcribed bank statement with arithmetic only.

Usage: python verify.py statement.json

The JSON is one statement object or a list of them (see references/data-format.md).
Exit 0 when every check passes, 1 otherwise. Prints one line per failure.

Nothing here reads the PDF. These checks prove the transcription is internally
consistent with the bank's own printed balances and totals; they cannot prove a
row exists that you never transcribed AND whose amount nets to zero.
"""
import json
import sys
from decimal import Decimal, InvalidOperation

CENT = Decimal("0.01")


def money(v, where):
    if v is None or v == "":
        return None
    try:
        return Decimal(str(v).replace(",", "")).quantize(CENT)
    except InvalidOperation:
        raise ValueError(f"{where}: not a money value: {v!r}")


def verify_statement(st, label="statement"):
    """Return a list of failure messages (empty = passed)."""
    errs = []
    opening = money(st.get("opening_balance"), f"{label} opening_balance")
    closing = money(st.get("closing_balance"), f"{label} closing_balance")
    if opening is None:
        errs.append(f"{label}: opening_balance missing")
        return errs

    rows = st.get("rows") or []
    running = opening      # last printed balance (or opening)
    pending = Decimal("0")  # net movement since that balance
    d_total = c_total = Decimal("0")
    d_count = c_count = 0

    for i, r in enumerate(rows, 1):
        where = f"{label} row {i} ({r.get('date')}, {str(r.get('raw') or r.get('description') or '')[:40]!r})"
        d = money(r.get("debit"), where)
        c = money(r.get("credit"), where)
        if d is not None and c is not None:
            errs.append(f"{where}: has both debit and credit")
        if d is None and c is None:
            errs.append(f"{where}: has neither debit nor credit")
        if d is not None:
            d_total += d
            d_count += 1
            pending -= d
        if c is not None:
            c_total += c
            c_count += 1
            pending += c
        bal = money(r.get("balance"), where)
        if bal is not None:
            expected = running + pending
            if expected != bal:
                errs.append(
                    f"{where}: balance chain broken: expected {expected}, printed {bal} "
                    f"(off by {bal - expected})"
                )
            running, pending = bal, Decimal("0")

    end = running + pending
    if closing is None:
        errs.append(f"{label}: closing_balance missing")
    elif end != closing:
        errs.append(f"{label}: opening {opening} + credits {c_total} - debits {d_total} = {end}, closing is {closing}")

    summary = st.get("summary") or {}
    for key, got in (("debit_total", d_total), ("credit_total", c_total)):
        want = money(summary.get(key), f"{label} summary.{key}")
        if want is not None and want != got:
            errs.append(f"{label}: {key} printed {want}, rows sum to {got}")
    for key, got in (("debit_count", d_count), ("credit_count", c_count)):
        want = summary.get(key)
        if want is not None and int(want) != got:
            errs.append(f"{label}: {key} printed {want}, rows count {got}")

    if st.get("closing_is_derived") and not any(
        summary.get(k) is not None for k in ("debit_total", "credit_total", "debit_count", "credit_count")
    ):
        errs.append(f"{label}: closing is derived from rows and no printed totals exist - nothing independent to check against")
    return errs


def verify_all(statements):
    if isinstance(statements, dict):
        statements = [statements]
    errs = []
    prev = None
    for n, st in enumerate(statements, 1):
        label = st.get("statement_date") or st.get("period_end") or f"statement {n}"
        errs += verify_statement(st, label)
        if prev is not None:
            a = money(prev.get("closing_balance"), "previous closing")
            b = money(st.get("opening_balance"), "opening")
            if a != b:
                errs.append(f"{label}: opening {b} does not equal previous statement's closing {a}")
        prev = st
    return errs


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        data = json.load(f)
    errs = verify_all(data)
    n = len(data) if isinstance(data, list) else 1
    rows = sum(len(s.get("rows") or []) for s in (data if isinstance(data, list) else [data]))
    if errs:
        print(f"FAILED: {len(errs)} problem(s) in {n} statement(s), {rows} row(s)")
        for e in errs:
            print("  - " + e)
        return 1
    print(f"PASSED: {n} statement(s), {rows} row(s) - balance chain, totals, counts and continuity all agree")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
