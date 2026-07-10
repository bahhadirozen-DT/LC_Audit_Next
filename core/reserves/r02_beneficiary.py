from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "beneficiary", None) == getattr(invoice, "seller", None)
    return ReserveResult(
        ok,
        "Beneficiary",
        "Beneficiary matches" if ok else "Beneficiary mismatch",
        "HIGH",
    )
