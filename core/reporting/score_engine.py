class ScoreEngine:

    def calculate(self, issues):

        score = 100

        for i in issues:

            sev = i["severity"]

            if sev == "KRİTİK":
                score -= 15

            elif sev == "YÜKSEK":
                score -= 8

            elif sev == "UYARI":
                score -= 2

            elif sev == "BİLGİ":
                score -= 0

        score = max(score, 0)

        if score >= 90:
            grade = "A"

        elif score >= 80:
            grade = "B"

        elif score >= 70:
            grade = "C"

        elif score >= 60:
            grade = "D"

        else:
            grade = "F"

        return {
            "score": score,
            "grade": grade,
        }
