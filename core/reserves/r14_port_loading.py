from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    ok = getattr(lc, "port_of_loading", None) == getattr(bl, "port_of_loading", None)

    return ReserveResult(
        ok,
        "Port of Loading",
        "Loading port matches" if ok else "Loading port mismatch",
        "HIGH",
    )
