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
            expected = rule.get("beklenen")

            value = getattr(document, field, None)

            rule_type = rule.get("tip")

            if rule_type == "esitlik":
                status = "PASS" if value == expected else "FAIL"

            elif rule_type == "varlik":
                status = "PASS" if value is not None else "FAIL"

            elif rule_type == "ibraz_suresi":
                if value is not None:
                    status = "PASS"
                else:
                    status = "PASS"
                    value = "21 days default (UCP600 Art 14)"

            elif rule_type == "liste_iceriyor":
                if isinstance(value, list):
                    status = "PASS" if expected in value else "FAIL"
                else:
                    status = "FAIL"

            elif rule_type == "tarih_varmi":
                status = "PASS" if value is not None else "FAIL"

            elif rule_type == "tolerans":
                if value and "/" in str(value):
                    status = "PASS"
                else:
                    status = "FAIL"

            else:
                status = "UNKNOWN"

            results.append({
                "madde": rule["madde"],
                "status": status,
                "alan": field,
                "deger": value,
                "aciklama": rule["aciklama"]
            })

        return results
