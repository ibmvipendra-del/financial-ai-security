from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END,
)

from src.planner import Planner
from src.executor import Executor
from src.response_generator import ResponseGenerator


planner = Planner()

executor = Executor()

generator = ResponseGenerator()


class AgentState(TypedDict):

    question: str

    plan: dict

    tool_result: str

    answer: str


# -----------------------------------
# Planner Node
# -----------------------------------

def planner_node(state: AgentState):

    plan = planner.plan(
        state["question"]
    )

    return {

        "question": state["question"],

        "plan": plan,

    }


# -----------------------------------
# Executor Node
# -----------------------------------

def executor_node(state: AgentState):

    result = executor.execute(
        state["plan"]
    )

    return {

        "question": state["question"],

        "plan": state["plan"],

        "tool_result": result["tool_result"],

        "answer": result["answer"],

    }


# -----------------------------------
# Response Generator
# -----------------------------------

def response_node(state: AgentState):

    if state["plan"]["tool"] == "chat":

        answer = generator.llm.invoke(
            state["question"]
        )

    else:

        answer = generator.generate(

            question=state["question"],

            tool_result=state["tool_result"],

        )

    return {

        "question": state["question"],

        "plan": state["plan"],

        "tool_result": state["tool_result"],

        "answer": answer,

    }


# -----------------------------------
# Build Graph
# -----------------------------------

builder = StateGraph(AgentState)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "executor",
    executor_node,
)

builder.add_node(
    "response",
    response_node,
)

builder.set_entry_point(
    "planner"
)

builder.add_edge(
    "planner",
    "executor",
)

builder.add_edge(
    "executor",
    "response",
)

builder.add_edge(
    "response",
    END,
)

graph = builder.compile()