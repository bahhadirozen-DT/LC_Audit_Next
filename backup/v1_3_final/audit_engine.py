from core.loaders.document_loader import DocumentLoader
from core.factory.parser_factory import ParserFactory


class AuditEngine:

    def __init__(self):

        self.loader = DocumentLoader()
        self.factory = ParserFactory()

    def load_and_parse(self, filename):

        text = self.loader.load(filename)

        return self.factory.parse(text)
