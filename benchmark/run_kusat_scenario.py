from pathlib import Path

print("=" * 70)
print("LC_Audit_Next - KUSAT Benchmark")
print("=" * 70)

scenario = Path("tests/scenarios/kusat")

if not scenario.exists():
    print("Scenario directory not found:")
    print(scenario)
    raise SystemExit(1)

print("Scenario found.")
print()

for f in sorted(scenario.glob("*.txt")):
    print(" -", f.name)

print()
print("Benchmark runner skeleton created.")
print("Next step: integrate AuditEngine.")
