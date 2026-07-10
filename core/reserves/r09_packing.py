from core.reserves.base_reserve import ReserveResult

def check(lc, packing):
    ok = getattr(lc, "packing", None) == getattr(packing, "packages", None)
    return ReserveResult(ok, "Packing",
                         "Packing matches" if ok else "Packing mismatch",
                         "MEDIUM")
