from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    allowed = getattr(lc, "transshipment", None)
    actual = getattr(bl, "transshipment", None)

    ok = (allowed == actual) or (allowed is None)

    return ReserveResult(
        ok,
        "Transshipment",
        "Transshipment OK" if ok else "Transshipment violation",
        "HIGH",
    )
