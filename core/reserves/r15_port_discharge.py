from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    ok = getattr(lc, "port_of_discharge", None) == getattr(bl, "port_of_discharge", None)

    return ReserveResult(
        ok,
        "Port of Discharge",
        "Discharge port matches" if ok else "Discharge port mismatch",
        "HIGH",
    )
