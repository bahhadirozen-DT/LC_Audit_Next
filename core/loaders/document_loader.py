from pathlib import Path

from core.loaders.pdf_loader import PDFLoader
from core.loaders.docx_loader import DOCXLoader


class DocumentLoader:

    def __init__(self):

        self.pdf = PDFLoader()
        self.docx = DOCXLoader()

    def load(self, filename):

        ext = Path(filename).suffix.lower()

        if ext == ".txt":
            return Path(filename).read_text(
                encoding="utf-8"
            )

        if ext == ".pdf":
            return self.pdf.load(filename)

        if ext == ".docx":
            return self.docx.load(filename)

        raise ValueError(
            f"Unsupported file type: {ext}"
        )
