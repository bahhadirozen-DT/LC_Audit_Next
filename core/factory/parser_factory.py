from core.document_detection.document_detector import DocumentDetector

from core.parser_mt700 import parse_mt700

from core.parsers.commercial_invoice_parser import parse_commercial_invoice
from core.parsers.bill_of_lading_parser import parse_bill_of_lading
from core.parsers.packing_list_parser import parse_packing_list
from core.parsers.certificate_of_origin_parser import parse_certificate_of_origin
from core.parsers.insurance_certificate_parser import parse_insurance_certificate


class ParserFactory:

    def __init__(self):
        self.detector = DocumentDetector()

    def parse(self, text: str):

        result = self.detector.detect(text)

        doc_type = result["document_type"]

        if doc_type == "MT700":
            model = parse_mt700(text)

        elif doc_type == "COMMERCIAL_INVOICE":
            model = parse_commercial_invoice(text)

        elif doc_type == "BILL_OF_LADING":
            model = parse_bill_of_lading(text)

        elif doc_type == "PACKING_LIST":
            model = parse_packing_list(text)

        elif doc_type == "CERTIFICATE_OF_ORIGIN":
            model = parse_certificate_of_origin(text)

        elif doc_type == "INSURANCE_CERTIFICATE":
            model = parse_insurance_certificate(text)

        else:
            raise ValueError(
                f"Unsupported document type: {doc_type}"
            )

        return {
            "document_type": doc_type,
            "confidence": result["confidence"],
            "model": model
        }
