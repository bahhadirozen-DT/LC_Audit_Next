from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "quantity", None) == getattr(invoice, "quantity", None)
    return ReserveResult(ok, "Quantity",
                         "Quantity matches" if ok else "Quantity mismatch",
                         "HIGH")
