from core.audit_engine import AuditEngine


class MultiDocumentEngine:

    def __init__(self):
        self.engine = AuditEngine()

    def load_documents(self, files):

        documents = []

        for filename in files:

            parsed = self.engine.load_and_parse(filename)

            documents.append({
                "filename": filename,
                "document_type": parsed["document_type"],
                "confidence": parsed["confidence"],
                "model": parsed["model"]
            })

        return documents
