from core.audit_engine import AuditEngine
from core.cross_document_audit import CrossDocumentAudit
from core.rules.discrepancy_engine import DiscrepancyEngine
from core.reporting.executive_summary import ExecutiveSummary
from core.reporting.audit_report import AuditReport

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

    print(f"[OK] {r['document_type']:<25} <- {f}")

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

report = AuditReport()

outfile = report.save(
    "audit_report.txt",
    summary,
    issues,
)

print()
print("=" * 90)
print("AUDIT COMPLETED")
print("=" * 90)
print(f"Critical : {summary['critical']}")
print(f"Warning  : {summary['warning']}")
print(f"Info     : {summary['info']}")
print(f"Decision : {summary['decision_tr']}")
print()
print(f"Report saved -> {outfile}")
