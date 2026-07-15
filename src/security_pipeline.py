from src.prompt_injection import PromptInjectionDetector


class SecurityPipeline:
    """
    Central AI Security Pipeline.

    Every user prompt passes through this
    pipeline before reaching the planner or LLM.
    """

    def __init__(self):

        self.prompt_detector = PromptInjectionDetector()

        # Future detectors
        #
        # self.jailbreak_detector = JailbreakDetector()
        # self.tool_abuse_detector = ToolAbuseDetector()
        # self.memory_detector = MemoryPoisoningDetector()

    def scan(self, prompt: str):

        prompt_result = self.prompt_detector.scan(prompt)

        findings = {
            "prompt_injection": prompt_result,
        }

        overall_score = prompt_result["score"]

        overall_risk = prompt_result["risk"]

        safe = prompt_result["safe"]

        return {

            "safe": safe,

            "overall_score": overall_score,

            "overall_risk": overall_risk,

            "findings": findings,
        }