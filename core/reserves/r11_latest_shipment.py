from core.reserves.base_reserve import ReserveResult

def check(lc, bl):
    lc_date = getattr(lc, "latest_shipment_date", None)
    bl_date = getattr(bl, "shipment_date", None)

    ok = (
        lc_date is not None
        and bl_date is not None
        and bl_date <= lc_date
    )

    return ReserveResult(
        ok,
        "Latest Shipment",
        "Latest shipment valid" if ok else "Latest shipment exceeded",
        "CRITICAL",
    )
