import re


class DecisionExtractor:
    """
    Extracts the business decision from an LLM response.

    Phase 1:
        Rule-based extraction.

    Phase 2:
        LLM-assisted classification.

    Phase 3:
        Enterprise policy mapping.
    """

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNKNOWN = "UNKNOWN"

    def extract(self, response: str) -> str:

        if not response:
            return self.UNKNOWN

        text = response.lower()

        approval_patterns = [
            r"\bapproved\b",
            r"\bapprove\b",
            r"\blikely to be approved\b",
            r"\bloan approved\b",
            r"\byes\b",
            r"\beligible\b",
        ]

        rejection_patterns = [
            r"\brejected\b",
            r"\breject\b",
            r"\bloan rejected\b",
            r"\bdeclined\b",
            r"\bnot approved\b",
        ]

        review_patterns = [
            r"\bmanual review\b",
            r"\breview\b",
            r"\bfurther information\b",
            r"\binsufficient information\b",
            r"\bcannot determine\b",
        ]

        for pattern in approval_patterns:
            if re.search(pattern, text):
                return self.APPROVED

        for pattern in rejection_patterns:
            if re.search(pattern, text):
                return self.REJECTED

        for pattern in review_patterns:
            if re.search(pattern, text):
                return self.REVIEW_REQUIRED

        return self.UNKNOWN