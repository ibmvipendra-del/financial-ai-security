from src.tools import TOOL_REGISTRY


class SecurityValidator:
    """
    Validates the execution plan before any tool is executed.
    """

    def validate(self, plan: dict):

        tool = plan.get("tool")

        # Chat requests are always allowed
        if tool == "chat":
            return True

        # Tool must exist
        if tool not in TOOL_REGISTRY:
            raise ValueError(
                f"Security Error: Unauthorized tool '{tool}'"
            )

        # Reserved for future validation
        # - Prompt Injection
        # - PII Detection
        # - Risk Scoring
        # - Authorization
        # - Rate Limiting

        return True