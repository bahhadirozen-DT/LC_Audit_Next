from core.reserves.base_reserve import ReserveResult

def check(lc, insurance):
    lc_risk = str(getattr(lc, "insurance_risk", "")).upper()
    ins_risk = str(getattr(insurance, "insurance_risk", "")).upper()

    ok = lc_risk == "" or lc_risk == ins_risk

    return ReserveResult(
        ok,
        "Insurance Risk",
        "Insurance risks covered" if ok else "Insurance risk mismatch",
        "HIGH",
    )
