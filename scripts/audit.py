import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.audit_engine import AuditEngine
from core.cross_document_audit import CrossDocumentAudit
from core.rules.discrepancy_engine import DiscrepancyEngine
from core.reporting.executive_summary import ExecutiveSummary
from core.reporting.audit_report import AuditReport
from core.reporting.score_engine import ScoreEngine

FILES = [
    "tests/Kusat.pdf",
    "tests/commercial invoice.pdf",
    "tests/packing list.docx",
    "tests/BILL OF LADING.docx",
    "tests/certificate of origin.docx",
    "tests/insurance certificate.docx",
]

engine = AuditEngine()
docs = {}

print("=" * 90)
print("LC AUDIT STARTED")
print("=" * 90)

for f in FILES:
    r = engine.load_and_parse(f)
    docs[r["document_type"]] = r["model"]

rows = CrossDocumentAudit().compare(
    mt700=docs.get("MT700"),
    invoice=docs.get("COMMERCIAL_INVOICE"),
    packing=docs.get("PACKING_LIST"),
    bl=docs.get("BILL_OF_LADING"),
    co=docs.get("CERTIFICATE_OF_ORIGIN"),
    insurance=docs.get("INSURANCE_CERTIFICATE"),
)

issues = DiscrepancyEngine().evaluate(rows)

summary = ExecutiveSummary().build(issues)
summary.update(ScoreEngine().calculate(issues))

report = AuditReport().build(summary, issues)

with open("audit_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("\n✅ audit_report.txt generated")
