from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = float(getattr(lc, "amount", 0)) == float(getattr(invoice, "total_amount", 0))
    return ReserveResult(
        ok,
        "Invoice Amount",
        "Invoice amount matches" if ok else "Invoice amount mismatch",
        "CRITICAL",
    )
