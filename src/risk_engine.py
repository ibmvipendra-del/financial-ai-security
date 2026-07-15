class RiskEngine:

    """
    Calculate AI security risk score.
    """

    WEIGHTS = {
        "ignore\\s+previous": 30,
        "ignore\\s+all": 30,
        "forget\\s+previous": 25,
        "system\\s+prompt": 35,
        "developer\\s+message": 35,
        "reveal\\s+prompt": 35,
        "show\\s+prompt": 30,
        "print\\s+prompt": 30,
        "api\\s*key": 40,
        "password": 40,
        "delete\\s+database": 50,
        "shutdown": 50,
        "sudo": 45,
        "rm\\s+-rf": 60,
        "bypass": 30,
        "override": 30,
        "disable\\s+security": 60,
        "ignore\\s+instructions": 35,
    }

    def calculate(self, matches):

        score = 0

        for match in matches:
            score += self.WEIGHTS.get(match, 20)

        score = min(score, 100)

        if score < 20:
            level = "LOW"
        elif score < 50:
            level = "MEDIUM"
        elif score < 80:
            level = "HIGH"
        else:
            level = "CRITICAL"

        return {
            "score": score,
            "level": level,
        }