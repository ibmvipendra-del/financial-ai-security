from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END,
)

from src.planner import Planner
from src.executor import Executor
from src.response_generator import ResponseGenerator
from src.hallucination_detector import HallucinationDetector
from src.output_guardrail import OutputGuardrail


planner = Planner()
executor = Executor()
generator = ResponseGenerator()

hallucination = HallucinationDetector()
guardrail = OutputGuardrail()


class AgentState(TypedDict):

    question: str

    plan: dict

    tool_result: str

    ground_truth: object

    hallucination: dict

    output_guardrail: dict

    answer: str


# -------------------------------------------------
# Planner
# -------------------------------------------------

def planner_node(state: AgentState):

    plan = planner.plan(state["question"])

    return {

        "question": state["question"],

        "plan": plan,

    }


# -------------------------------------------------
# Executor
# -------------------------------------------------

def executor_node(state: AgentState):

    result = executor.execute(state["plan"])

    return {

        "question": state["question"],

        "plan": state["plan"],

        "tool_result": result["tool_result"],

        "ground_truth": result["ground_truth"],

        "answer": result["answer"],

    }


# -------------------------------------------------
# Response Generator
# -------------------------------------------------

def response_node(state: AgentState):

    # ---------------------------------
    # Chat
    # ---------------------------------

    if state["plan"]["tool"] == "chat":

        answer = generator.llm.invoke(
            state["question"]
        )

        guard_result = guardrail.scan(answer)

        if not guard_result["safe"]:

            answer = (
                "Response blocked by Output Guardrail."
            )

        return {

            "question": state["question"],

            "plan": state["plan"],

            "tool_result": None,

            "ground_truth": None,

            "hallucination": None,

            "output_guardrail": guard_result,

            "answer": answer,

        }

    # ---------------------------------
    # Financial Tool Response
    # ---------------------------------

    answer = generator.generate(

        question=state["question"],

        ground_truth=state["ground_truth"],

    )

    hallucination_result = hallucination.scan(

        state["ground_truth"],

        answer,

    )

    guard_result = guardrail.scan(answer)

    if not guard_result["safe"]:

        answer = (
            "Response blocked by Output Guardrail."
        )

    return {

        "question": state["question"],

        "plan": state["plan"],

        "tool_result": state["tool_result"],

        "ground_truth": state["ground_truth"],

        "hallucination": hallucination_result,

        "output_guardrail": guard_result,

        "answer": answer,

    }


# -------------------------------------------------
# Build Graph
# -------------------------------------------------

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)

builder.add_node("executor", executor_node)

builder.add_node("response", response_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "executor")

builder.add_edge("executor", "response")

builder.add_edge("response", END)

graph = builder.compile()