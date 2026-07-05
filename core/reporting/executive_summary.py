class ExecutiveSummary:

    def build(self, issues):

        critical = sum(i["severity"] == "KRİTİK" for i in issues)
        warning = sum(i["severity"] == "UYARI" for i in issues)
        info = sum(i["severity"] == "BİLGİ" for i in issues)

        if critical >= 5:
            overall = "VERY HIGH"
            decision = "DO NOT PRESENT"
            decision_tr = "İBRAZ ETMEYİN"

        elif critical >= 3:
            overall = "HIGH"
            decision = "PRESENT AFTER CORRECTION"
            decision_tr = "DÜZELTİLDİKTEN SONRA İBRAZ EDİN"

        elif critical >= 1:
            overall = "MEDIUM"
            decision = "PRESENT WITH CAUTION"
            decision_tr = "DİKKATLİ İBRAZ"

        else:
            overall = "LOW"
            decision = "READY FOR PRESENTATION"
            decision_tr = "İBRAZA UYGUN"

        return {
            "critical": critical,
            "warning": warning,
            "info": info,
            "overall_risk": overall,
            "decision_en": decision,
            "decision_tr": decision_tr,
        }
