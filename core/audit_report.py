class AuditReport:

    def __init__(self, results):
        self.results = results

    def summary(self):
        total = len(self.results)

        passed = sum(
            1 for r in self.results
            if r["status"] == "PASS"
        )

        failed = sum(
            1 for r in self.results
            if r["status"] == "FAIL"
        )

        return {
            "total": total,
            "passed": passed,
            "failed": failed
        }

    def to_dict(self):
        return {
            "document": "MT700",
            "summary": self.summary(),
            "results": self.results,
            "issues": [
                r for r in self.results
                if r["status"] == "FAIL"
            ]
        }
