from core.rules.risk_matrix import RISK_MATRIX

class DiscrepancyEngine:

    def evaluate(self, rows):

        issues = []

        for r in rows:

            status = r["status"]

            if status == "PASS":
                continue

            if status == "PASS_WITH_NORMALIZATION":

                severity = "UYARI"

                comment = (
                    "Değerler normalizasyon uygulanarak eşleşti. "
                    "Yazım biçimi farklı olsa da içerik aynı görünüyor. "
                    "Rezerv oluşturması beklenmez, ancak nihai kontrol kullanıcı sorumluluğundadır."
                )

            elif status == "UNKNOWN":

                severity = "BİLGİ"

                comment = (
                    "Karşılaştırma için yeterli veri bulunamadı."
                )

            else:

                critical_checks = {
                    "Applicant / Buyer",
                    "Beneficiary / Seller",
                    "Amount",
                    "Currency",
                    "Goods Description",
                    "Goods",
                    "Shipper",
                    "Consignee",
                    "Insured",
                }

                if r["check"] in critical_checks:
                    info=RISK_MATRIX.get(r["check"],{})
severity=info.get("severity","KRİTİK")
                else:
                    severity = "UYARI"

                comment = "MT700 şartları ile belge arasında uyumsuzluk bulundu."

            issues.append({
                "severity": severity,
                "document": r["document"],
                "check": r["check"],
                "status": status,
                "comment": comment,
                "ucp": info.get("ucp","-"),
                "isbp": info.get("isbp","-"),
                "explanation": info.get("tr",""),
            })

        return issues
