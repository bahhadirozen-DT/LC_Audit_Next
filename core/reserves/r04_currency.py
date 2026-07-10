from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "currency", None) == getattr(invoice, "currency", None)
    return ReserveResult(
        ok,
        "Currency",
        "Currency matches" if ok else "Currency mismatch",
        "HIGH",
    )
