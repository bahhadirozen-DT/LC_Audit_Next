from core.loaders.document_loader import DocumentLoader
from core.factory.parser_factory import ParserFactory

from core.rules_engine import RulesEngine
from core.similarity.similarity_engine import SimilarityEngine


class AuditEngine:

    def __init__(self):

        self.loader = DocumentLoader()
        self.factory = ParserFactory()

        self.rules = RulesEngine()
        self.similarity = SimilarityEngine()

    def load_and_parse(self, filename):

        text = self.loader.load(filename)

        return self.factory.parse(text)

    def audit(self, filename):

        model = self.load_and_parse(filename)

        rule_results = self.rules.audit(model)

        similarity = {}

        try:
            similarity = self.similarity.compare(model)
        except Exception:
            similarity = {}

        return {
            "model": model,
            "rules": rule_results,
            "similarity": similarity,
        }
