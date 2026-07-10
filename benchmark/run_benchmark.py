from pathlib import Path
import json
from core.audit_engine import AuditEngine

SCENARIOS = Path("benchmark/scenarios")
EXPECTED = Path("benchmark/expected")
RESULTS = Path("benchmark/results")

engine = AuditEngine()

total_expected = 0
total_found = 0
correct = 0

print("=" * 70)
print("LC_Audit_Next Benchmark")
print("=" * 70)

for scenario in sorted(SCENARIOS.iterdir()):

    if not scenario.is_dir():
        continue

    print(f"\nScenario : {scenario.name}")

    docs = {}

    VALID_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt"}

for f in scenario.iterdir():
    if (
        f.is_file()
        and f.suffix.lower() in VALID_EXTENSIONS
    ):
        docs[f.stem.upper()] = str(f)

    

    report = engine.audit_folder(str(scenario))

    found = []

    for r in report.get("cross_results", []):

        if isinstance(r, str):
            found.append(r.upper())

        elif hasattr(r, "code"):
            found.append(str(r.code).upper())

        elif hasattr(r, "field"):
            found.append(str(r.field).upper())

    found = sorted(set(found))

expected_file = EXPECTED / f"{scenario.name}.json"

    if expected_file.exists():
        expected = sorted(json.loads(expected_file.read_text()))
    else:
        expected = []

    tp = len(set(found) & set(expected))

    total_expected += len(expected)
    total_found += len(found)
    correct += tp

    print("Expected :", expected)
    print("Found    :", found)

precision = correct / total_found if total_found else 0
recall = correct / total_expected if total_expected else 0

f1 = 0
if precision + recall:
    f1 = 2 * precision * recall / (precision + recall)

print("\n" + "=" * 70)
print("FINAL RESULT")
print("=" * 70)
print(f"Expected reserves : {total_expected}")
print(f"Detected reserves : {total_found}")
print(f"Correct           : {correct}")
print(f"Precision         : {precision:.3f}")
print(f"Recall            : {recall:.3f}")
print(f"F1 Score          : {f1:.3f}")
print("=" * 70)
