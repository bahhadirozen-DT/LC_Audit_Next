from core.document_detection.document_detector import DocumentDetector
from core.parser_mt700 import parse_mt700
from core.parsers.commercial_invoice_parser import parse_commercial_invoice


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

        else:
            raise ValueError(f"Unsupported document type: {doc_type}")

        return {
            "document_type": doc_type,
            "confidence": result["confidence"],
            "model": model
        }
