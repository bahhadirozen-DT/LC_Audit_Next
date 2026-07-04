import re
import unicodedata


class ValueComparer:

    @staticmethod
    def normalize_text(value):

        if value is None:
            return None

        s = str(value).upper().strip()

        # Türkçe karakterleri ASCII'ye çevir
        s = unicodedata.normalize("NFKD", s)
        s = s.encode("ascii", "ignore").decode()

        # Firma kısaltmaları
        s = re.sub(r"\bA\.?\s*S\.?\b", "AS", s)
        s = re.sub(r"\bLIMITED\b", "LTD", s)
        s = re.sub(r"\bLTD\.?\b", "LTD", s)
        s = re.sub(r"\bINCORPORATED\b", "INC", s)
        s = re.sub(r"\bCOMPANY\b", "CO", s)

        # Noktalama temizliği
        s = re.sub(r"[.,;/\-]", " ", s)

        # Çoklu boşluk
        s = re.sub(r"\s+", " ", s).strip()

        return s

    @staticmethod
    def normalize_number(value):

        if value is None:
            return None

        s = str(value).upper().strip()

        for token in (
            "USD",
            "EUR",
            "TRY",
            "GBP",
            "KG",
            "KGS",
            "CBM",
        ):
            s = s.replace(token, "")

        s = s.replace(" ", "")

        # Avrupa: 2.000,00
        if "." in s and "," in s:

            if s.rfind(",") > s.rfind("."):
                s = s.replace(".", "")
                s = s.replace(",", ".")

            else:
                s = s.replace(",", "")

        elif "," in s:

            # 25,5
            if re.fullmatch(r"\d+,\d{1,2}", s):
                s = s.replace(",", ".")

            else:
                # 2,000
                s = s.replace(",", "")

        elif "." in s:

            # 25.5
            if re.fullmatch(r"\d+\.\d{1,2}", s):
                pass

            else:
                # 25.000
                s = s.replace(".", "")

        try:
            return float(s)
        except:
            return None

    @classmethod
    def compare(cls, left, right):

        if left is None or right is None:
            return {
                "status": "UNKNOWN",
                "reason": "Missing value",
            }

        ln = cls.normalize_number(left)
        rn = cls.normalize_number(right)

        if ln is not None and rn is not None:

            if abs(ln - rn) < 0.000001:
                return {
                    "status": "PASS_WITH_NORMALIZATION",
                    "reason": "Equivalent numeric values",
                }

            return {
                "status": "FAIL",
                "reason": "Numeric values differ",
            }

        lt = cls.normalize_text(left)
        rt = cls.normalize_text(right)

        if lt == rt:
            if str(left).strip() == str(right).strip():
                return {
                    "status": "PASS",
                    "reason": "Exact match",
                }

            return {
                "status": "PASS_WITH_NORMALIZATION",
                "reason": "Normalized text match",
            }

        if lt in rt or rt in lt:
            return {
                "status": "WARNING",
                "reason": "Partial text match",
            }

        return {
            "status": "FAIL",
            "reason": "Values differ",
        }
