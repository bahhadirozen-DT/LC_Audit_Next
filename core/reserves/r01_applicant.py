from core.reserves.base_reserve import ReserveResult

def check(lc, invoice):
    ok = getattr(lc, "applicant", None) == getattr(invoice, "buyer", None)
    return ReserveResult(
        ok,
        "Applicant",
        "Applicant matches" if ok else "Applicant mismatch",
        "HIGH",
    )
