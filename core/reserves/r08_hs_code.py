from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "hs_code", None) == getattr(invoice, "hs_code", None)
    return ReserveResult(ok, "HS Code",
                         "HS Code matches" if ok else "HS Code mismatch",
                         "HIGH")
