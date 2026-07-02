from pathlib import Path


class DocumentLoader:

    def load(self, filename):

        ext = Path(filename).suffix.lower()

        if ext == ".txt":
            return Path(filename).read_text(
                encoding="utf-8"
            )

        raise ValueError(
            f"Unsupported file type: {ext}"
        )
