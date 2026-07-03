from pathlib import Path

try:
    import pypdf
except ImportError:
    pypdf = None


class PDFLoader:

    def load(self, filename):

        if pypdf is None:
            raise ImportError(
                "pypdf is not installed. Run: pip install pypdf"
            )

        reader = pypdf.PdfReader(filename)

        text = []

        for page in reader.pages:

            content = page.extract_text()

            if content:
                text.append(content)

        return "\n".join(text)
