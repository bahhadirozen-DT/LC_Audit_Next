from pathlib import Path

from core.loaders.document_loader import DocumentLoader
from core.factory.parser_factory import ParserFactory

from core.rules_engine import RulesEngine
from core.similarity.similarity_engine import SimilarityEngine
from core.cross_validation.cross_document_validator import CrossDocumentValidator


class AuditEngine:

    def __init__(self):
        self.loader = DocumentLoader()
        self.factory = ParserFactory()

        self.rules = RulesEngine()
        self.similarity = SimilarityEngine()
        self.cross = CrossDocumentValidator()

    def load_and_parse(self, filename):
        text = self.loader.load(filename)
        return self.factory.parse(text)

    def audit(self, filename):

        parsed = self.load_and_parse(filename)
        model = parsed["model"]

        rules = self.rules.audit(model)

        try:
            similarity = self.similarity.compare(model)
        except Exception:
            similarity = {}

        return {
            "document_type": parsed["document_type"],
            "confidence": parsed["confidence"],
            "model": model,
            "rules": rules,
            "similarity": similarity,
        }

    def audit_folder(self, folder):

        folder = Path(folder)

        models = []

        for file in sorted(folder.iterdir()):

            if file.suffix.lower() not in {
                ".pdf",
                ".docx",
                ".doc",
                ".txt",
            }:
                continue

            try:
                parsed = self.load_and_parse(str(file))
                models.append(parsed["model"])
            except Exception as e:
                print(f"SKIP {file.name}: {e}")

        try:
            cross_results = self.cross.validate(models)
        except Exception:
            cross_results = []

        return {
            "documents": models,
            "cross_results": cross_results,
        }
