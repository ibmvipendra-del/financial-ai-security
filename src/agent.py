from typing import TypedDict

from langgraph.graph import StateGraph, END

from src.tools import emergency_fund


class AgentState(TypedDict):
    question: str
    answer: str


def router(state: AgentState):

    question = state["question"].lower()

    if "emergency" in question:
        return "emergency_node"

    return "chat_node"


def emergency_node(state: AgentState):

    result = emergency_fund.invoke(
        {
            "monthly_expense": 50000
        }
    )

    return {
        "question": state["question"],
        "answer": result,
    }


def chat_node(state: AgentState):

    return {
        "question": state["question"],
        "answer": (
            "General Chat Node. LLM integration is coming next."
        ),
    }


workflow = StateGraph(AgentState)

workflow.add_node("emergency_node", emergency_node)
workflow.add_node("chat_node", chat_node)

workflow.set_conditional_entry_point(
    router,
    {
        "emergency_node": "emergency_node",
        "chat_node": "chat_node",
    },
)

workflow.add_edge("emergency_node", END)
workflow.add_edge("chat_node", END)

app = workflow.compile()