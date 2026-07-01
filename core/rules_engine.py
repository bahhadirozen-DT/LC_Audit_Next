import json
from pathlib import Path


class RulesEngine:

    def __init__(self, rules_path="knowledge/rules/kurallar.json"):
        self.rules_path = Path(rules_path)
        self.rules = self.load_rules()

    def load_rules(self):
        with open(self.rules_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def audit(self, document):

        results = []

        for rule in self.rules["kurallar"]:

            field = rule["alan"]
            expected = rule["beklenen"]

            value = getattr(document, field, None)

            if value == expected:
                status = "PASS"
            else:
                status = "FAIL"

            results.append({
                "madde": rule["madde"],
                "status": status,
                "alan": field,
                "deger": value,
                "aciklama": rule["aciklama"]
            })

        return results
