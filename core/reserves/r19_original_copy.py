from core.validation.original_copy_validator import OriginalCopyValidator

def check(lc, docs):
    return OriginalCopyValidator().validate(lc, docs)
