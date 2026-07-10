from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    allowed = getattr(lc, "partial_shipment", None)
    actual = getattr(bl, "partial_shipment", None)

    ok = (allowed == actual) or (allowed is None)

    return ReserveResult(
        ok,
        "Partial Shipment",
        "Partial shipment OK" if ok else "Partial shipment violation",
        "HIGH",
    )
