from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    ok = getattr(lc, "notify_party", None) == getattr(bl, "notify_party", None)
    return ReserveResult(
        ok,
        "Notify Party",
        "Notify party matches" if ok else "Notify party mismatch",
        "HIGH",
    )
