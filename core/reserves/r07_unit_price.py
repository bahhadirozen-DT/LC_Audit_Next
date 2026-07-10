from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "unit_price", None) == getattr(invoice, "unit_price", None)
    return ReserveResult(ok, "Unit Price",
                         "Unit price matches" if ok else "Unit price mismatch",
                         "MEDIUM")
