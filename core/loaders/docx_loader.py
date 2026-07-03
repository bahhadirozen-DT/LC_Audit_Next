from docx import Document


class DOCXLoader:

    def load(self, filename):

        doc = Document(filename)

        text = []

        for p in doc.paragraphs:
            if p.text.strip():
                text.append(p.text)

        return "\n".join(text)
