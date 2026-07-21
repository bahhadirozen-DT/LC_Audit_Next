from pathlib import Path

from core.audit_engine import AuditEngine
from core.document_detection.document_detector import DocumentDetector

ROOT = Path("tests/scenarios/kusat")

print("=" * 70)
print("LC_Audit_Next Benchmark")
print("=" * 70)

detector = DocumentDetector()
engine = AuditEngine()

documents = {}

for file in sorted(ROOT.glob("*.txt")):

    text = file.read_text(encoding="utf-8")

    result = detector.detect(text)
    doc_type = result["document_type"]

    documents[doc_type] = text

    print(f"{file.name:35} -> {doc_type} ({result['confidence']})")

print()

print("Loaded documents :", len(documents))
print()

if len(documents) < 6:
    print("Scenario is incomplete.")
    raise SystemExit(1)

print("Running AuditEngine...")
print()

result = engine.audit_folder(ROOT)

print("=" * 70)
print("AUDIT RESULT")
print("=" * 70)
print(result)

