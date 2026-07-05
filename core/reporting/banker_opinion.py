class BankerOpinion:

    def build(self, summary, issues):

        critical = summary["critical"]
        warning = summary["warning"]
        info = summary["info"]

        score = summary.get("score", 0)

        if critical >= 5:
            decision_tr = "İBRAZ ETMEYİN"
            decision_en = "DO NOT PRESENT"

        elif critical >= 2:
            decision_tr = "DÜZELTİLDİKTEN SONRA İBRAZ EDİN"
            decision_en = "PRESENT AFTER CORRECTION"

        else:
            decision_tr = "İBRAZ EDİLEBİLİR"
            decision_en = "READY FOR PRESENTATION"

        report = []

        report.append("=" * 90)
        report.append("BANKER'S OPINION")
        report.append("=" * 90)
        report.append("")

        report.append("TÜRKÇE")
        report.append("")

        report.append(
            f"Belgelerde toplam {len(issues)} adet bulgu tespit edilmiştir."
        )

        report.append(
            f"Bunların {critical} adedi kritik,"
            f" {warning} adedi uyarı,"
            f" {info} adedi bilgilendirme seviyesindedir."
        )

        report.append("")

        report.append(
            "Değerlendirme UCP600 ve ISBP kuralları dikkate alınarak yapılmıştır."
        )

        report.append(
            f"Genel denetim puanı: {score}/100"
        )

        report.append(
            f"Sonuç: {decision_tr}"
        )

        report.append("")
        report.append("-" * 90)
        report.append("")

        report.append("ENGLISH")
        report.append("")

        report.append(
            f"{len(issues)} discrepancies were identified."
        )

        report.append(
            f"{critical} critical, {warning} warning and {info} informational findings."
        )

        report.append(
            "The evaluation has been performed according to UCP600 and ISBP."
        )

        report.append(
            f"Overall audit score: {score}/100"
        )

        report.append(
            f"Decision: {decision_en}"
        )

        return "\n".join(report)
