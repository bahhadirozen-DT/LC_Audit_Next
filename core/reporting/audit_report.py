from datetime import datetime
from core.rules.rule_library import RULE_LIBRARY
from core.reporting.banker_opinion import BankerOpinion


class AuditReport:

    def build(self, summary, issues):

        lines = []

        lines.append("=" * 100)
        lines.append("LC AUDIT REPORT")
        lines.append("=" * 100)
        lines.append("")

        lines.append("EXECUTIVE SUMMARY")
        lines.append("-" * 100)
        lines.append(f"Overall Risk          : {summary['overall_risk']}")
        lines.append(f"Recommendation (EN)   : {summary['decision_en']}")
        lines.append(f"Recommendation (TR)   : {summary['decision_tr']}")
        lines.append("")
        lines.append(f"Critical : {summary['critical']}")
        lines.append(f"Warning  : {summary['warning']}")
        lines.append(f"Info     : {summary['info']}")
        lines.append("")
        lines.append("=" * 100)

        for i, issue in enumerate(issues, 1):

            lines.append("")
            lines.append(f"[{i}] {issue['check']}")
            lines.append("-" * 100)

            lines.append(f"Belge (Document)      : {issue['document']}")
            lines.append(f"Önem Derecesi         : {issue['severity']}")
            lines.append(f"Durum                : {issue['status']}")
            lines.append("")

            lines.append(f"Türkçe Alan          : {issue.get('title_tr','')}")
            lines.append(f"English Field        : {issue.get('title_en','')}")
            lines.append("")

            lines.append(f"UCP600               : {issue.get('ucp','-')}")
            lines.append(f"ISBP                 : {issue.get('isbp','-')}")
            lines.append("")

            lines.append("UCP Açıklaması")
            lines.append(issue.get("ucp_tr", "-"))
            lines.append("")

            lines.append("ISBP Açıklaması")
            lines.append(issue.get("isbp_tr", "-"))
            lines.append("")

            lines.append("Banka Yorumu")
            lines.append(issue.get("explanation", "-"))
            lines.append("")

            lines.append(
                f"Rezerv Olasılığı     : %{issue.get('reservation_probability','-')}"
            )
            lines.append("")

            lines.append("Önerilen İşlem")
            lines.append(issue.get("action", "-"))
            lines.append("")

            lines.append("=" * 100)


        lines.append("")
        lines.append(BankerOpinion().build(summary, issues))

        return "\n".join(lines)


    def save(self, filename, summary, issues):

        report = self.build(summary, issues)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)

        return filename
