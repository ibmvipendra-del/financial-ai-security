from typing import TypedDict
import re

from langgraph.graph import StateGraph, END

from src.tools import TOOL_REGISTRY
from src.llm import DummyLLM

llm = DummyLLM()


class AgentState(TypedDict):
    question: str
    answer: str


# -------------------------
# Router
# -------------------------

def router(state: AgentState):

    question = state["question"].lower()

    if "emergency" in question:
        return "tool"

    return "chat"


# -------------------------
# Helper
# -------------------------

def extract_amount(question: str):

    numbers = re.findall(r"\d+", question)

    if numbers:
        return float(numbers[0])

    return 50000


# -------------------------
# Tool Node
# -------------------------

def tool_node(state: AgentState):

    expense = extract_amount(state["question"])

    tool = TOOL_REGISTRY["emergency_fund"]

    result = tool.invoke(
        {
            "monthly_expense": expense
        }
    )

    return {
        "question": state["question"],
        "answer": result,
    }


# -------------------------
# Chat Node
# -------------------------

def chat_node(state: AgentState):

    response = llm.invoke(
        state["question"]
    )

    return {
        "question": state["question"],
        "answer": response
    }


builder = StateGraph(AgentState)

builder.add_node(
    "tool",
    tool_node
)

builder.add_node(
    "chat",
    chat_node
)

builder.set_conditional_entry_point(
    router,
    {
        "tool": "tool",
        "chat": "chat"
    }
)

builder.add_edge("tool", END)
builder.add_edge("chat", END)

graph = builder.compile()