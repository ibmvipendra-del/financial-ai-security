from typing import TypedDict

from langgraph.graph import StateGraph, END

from src.planner import Planner
from src.executor import ToolExecutor
from src.security_validator import SecurityValidator
from src.llm_factory import LLMFactory


planner = Planner()
executor = ToolExecutor()
validator = SecurityValidator()
llm = LLMFactory.create()


class AgentState(TypedDict, total=False):
    question: str
    plan: dict
    answer: str


# --------------------------------------------------
# Planner Node
# --------------------------------------------------
def planner_node(state: AgentState):

    plan = planner.create_plan(state["question"])

    return {
        "question": state["question"],
        "plan": plan,
    }


# --------------------------------------------------
# Security Node
# --------------------------------------------------
def security_node(state: AgentState):

    validator.validate(state["plan"])

    return state


# --------------------------------------------------
# Execution Node
# --------------------------------------------------
def execution_node(state: AgentState):

    result = executor.execute(state["plan"])

    if result is None:
        result = llm.invoke(state["question"])

    return {
        "question": state["question"],
        "plan": state["plan"],
        "answer": result,
    }


# --------------------------------------------------
# Build Graph
# --------------------------------------------------

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("security", security_node)
builder.add_node("execution", execution_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "security")
builder.add_edge("security", "execution")
builder.add_edge("execution", END)

graph = builder.compile()