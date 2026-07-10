from core.validation.required_documents_validator import RequiredDocumentsValidator

def check(lc, docs):
    return RequiredDocumentsValidator().validate(lc, docs)
