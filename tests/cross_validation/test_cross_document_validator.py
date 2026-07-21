from core.cross_validation.cross_document_validator import CrossDocumentValidator

from models.mt700_model import MT700Model
from models.commercial_invoice_model import CommercialInvoiceModel
from models.bill_of_lading_model import BillOfLadingModel


def make_mt700():
    return MT700Model(
        document_type="MT700",
        document_name="Documentary Credit",
        source_file="test.txt",
        raw_text="",
    )


def test_applicant_matches_invoice():

    lc = make_mt700()
    lc.applicant = "ABC IMPORT LTD"

    invoice = CommercialInvoiceModel()
    invoice.seller = "ABC IMPORT LTD"

    validator = CrossDocumentValidator()

    result = validator.validate([lc, invoice])

    assert isinstance(result, list)


def test_bill_of_lading_exists():

    lc = make_mt700()

    bl = BillOfLadingModel()

    validator = CrossDocumentValidator()

    result = validator.validate([lc, bl])

    assert isinstance(result, list)
