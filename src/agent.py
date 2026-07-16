from src.graph import graph
from src.security_pipeline import SecurityPipeline
from src.audit_logger import AuditLogger
from src.policy_engine import PolicyEngine


class FinancialAIAgent:

    def __init__(self):

        self.security = SecurityPipeline()

        self.audit = AuditLogger()

        self.policy = PolicyEngine()

    def invoke(self, question: str):

        # -----------------------------------------
        # Run Input Security Pipeline
        # -----------------------------------------

        security_result = self.security.scan(question)

        # -----------------------------------------
        # Block Malicious Input Immediately
        # -----------------------------------------

        if not security_result.safe:

            blocked_response = {

                "question": question,

                "answer": "Request blocked by AI Security Pipeline.",

                "security": security_result,

            }

            self.audit.log({

                "question": question,

                "status": "BLOCKED",

                "reason": "Security Pipeline",

                "security": security_result,

            })

            return blocked_response

        # -----------------------------------------
        # Execute LangGraph
        # -----------------------------------------

        response = graph.invoke({

            "question": question

        })

        response["security"] = security_result

        # -----------------------------------------
        # Policy Evaluation
        # -----------------------------------------

        policy = self.policy.evaluate(

            security=security_result,

            hallucination=response.get("hallucination"),

            output_guardrail=response.get("output_guardrail"),

        )

        response["policy"] = policy

        # -----------------------------------------
        # Enforce Policy
        # -----------------------------------------

        if not policy.allow:

            response["answer"] = (

                "Response blocked by AI Policy Engine.\n"

                f"Reason: {policy.reason}"

            )

        # -----------------------------------------
        # Audit Logging
        # -----------------------------------------

        self.audit.log({

            "question": question,

            "status": (

                "BLOCKED"

                if not policy.allow

                else "SUCCESS"

            ),

            "reason": policy.reason,

            "policy": policy,

            "plan": response.get("plan"),

            "tool": response.get("plan", {}).get("tool"),

            "tool_result": response.get("tool_result"),

            "hallucination": response.get("hallucination"),

            "output_guardrail": response.get("output_guardrail"),

            "security": security_result,

        })

        return response