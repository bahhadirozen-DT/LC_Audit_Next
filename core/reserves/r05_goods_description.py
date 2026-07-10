from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    lc_goods = str(getattr(lc, "goods_description", "")).upper()
    inv_goods = str(getattr(invoice, "goods_description", "")).upper()

    ok = lc_goods == inv_goods

    return ReserveResult(
        ok,
        "Goods Description",
        "Goods match" if ok else "Goods mismatch",
        "CRITICAL",
    )
