from core.reserves.base_reserve import ReserveResult

def check(lc, insurance):
    lc_amount = getattr(lc, "insurance_amount", None)
    ins_amount = getattr(insurance, "insured_amount", None)

    ok = (
        lc_amount is None
        or ins_amount is None
        or ins_amount >= lc_amount
    )

    return ReserveResult(
        ok,
        "Insurance Amount",
        "Insurance amount valid" if ok else "Insurance amount insufficient",
        "HIGH",
    )
