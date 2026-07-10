from core.validation.required_documents_validator import RequiredDocumentsValidator


def test_required_documents():

    validator = RequiredDocumentsValidator()

    result = validator.validate(
        [
            "COMMERCIAL_INVOICE",
            "PACKING_LIST",
            "BILL_OF_LADING",
        ],
        [
            "COMMERCIAL_INVOICE",
            "PACKING_LIST",
        ],
    )

    assert result["status"] == "FAIL"
    assert result["missing"] == ["BILL_OF_LADING"]


def test_required_documents_pass():

    validator = RequiredDocumentsValidator()

    result = validator.validate(
        [
            "COMMERCIAL_INVOICE",
            "PACKING_LIST",
        ],
        [
            "COMMERCIAL_INVOICE",
            "PACKING_LIST",
        ],
    )

    assert result["status"] == "PASS"
