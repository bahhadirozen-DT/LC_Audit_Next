from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os


class PDFReport:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        # Unicode font (varsa)
        try:
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont("DejaVu", font_path))
                for s in self.styles.byName.values():
                    s.fontName = "DejaVu"
        except Exception:
            pass

    def build(self, filename, summary, issues):

        doc = SimpleDocTemplate(filename)

        story = []

        story.append(Paragraph("<b>LC AUDIT REPORT</b>", self.styles["Title"]))
        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                "<b>Executive Summary</b>",
                self.styles["Heading2"],
            )
        )

        table = Table(
            [
                ["Overall Risk", summary["overall_risk"]],
                ["Decision (EN)", summary["decision_en"]],
                ["Decision (TR)", summary["decision_tr"]],
                ["Critical", str(summary["critical"])],
                ["Warning", str(summary["warning"])],
                ["Information", str(summary["info"])],
                ["Score", f'{summary.get("score","-")} / 100'],
            ],
            colWidths=[170, 320],
        )

        table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                    ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                    ("FONTNAME", (0, 0), (-1, -1), "DejaVu"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )

        story.append(table)
        story.append(Spacer(1, 20))

        for i, issue in enumerate(issues, 1):

            story.append(
                Paragraph(
                    f"<b>{i}. {issue['check']}</b>",
                    self.styles["Heading2"],
                )
            )

            txt = f"""
<b>Document</b>: {issue['document']}<br/>
<b>Severity</b>: {issue['severity']}<br/>
<b>Status</b>: {issue['status']}<br/>
<b>UCP600</b>: {issue.get('ucp','-')}<br/>
<b>ISBP</b>: {issue.get('isbp','-')}<br/>
<b>Risk</b>: %{issue.get('reservation_probability','-')}<br/><br/>

<b>Türkçe Açıklama</b><br/>
{issue.get('explanation','-')}<br/><br/>

<b>Önerilen İşlem</b><br/>
{issue.get('action','-')}
"""

            story.append(Paragraph(txt, self.styles["BodyText"]))
            story.append(Spacer(1, 14))

        doc.build(story)
