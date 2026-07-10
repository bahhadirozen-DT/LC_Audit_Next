from core.validation.legalized_coo_validator import LegalizedCOOValidator

def check(lc, coo):
    return LegalizedCOOValidator().validate(lc, coo)
