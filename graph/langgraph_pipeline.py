from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.investigator import investigator_agent
from agents.risk_analyzer import risk_analyzer_agent
from agents.decision_agent import decision_agent
from observability.logger import PipelineLogger


# Shared state a todos los nodos
class PipelineState(TypedDict):
    alert_id: str
    context: dict
    analysis: dict
    decision: dict
    logger: PipelineLogger


# Nodo investigador
def investigator_node(state: PipelineState):
    context = investigator_agent(state["alert_id"])

    state["logger"].log(
        "investigator",
        {"alert_id": state["alert_id"]},
        context
    )

    return {"context": context}


# Nodo analista de riesgos
def risk_node(state: PipelineState):
    analysis = risk_analyzer_agent(state["context"])

    state["logger"].log(
        "risk_analyzer",
        state["context"],
        analysis
    )

    return {"analysis": analysis}


# Nodo de decisión
def decision_node(state: PipelineState):
    decision = decision_agent(state["analysis"])

    state["logger"].log(
        "decision_agent",
        state["analysis"],
        decision
    )

    return {"decision": decision}


# Contruyo el grafo
def build_graph():
    builder = StateGraph(PipelineState)

    builder.add_node("investigator", investigator_node)
    builder.add_node("risk", risk_node)
    builder.add_node("decision", decision_node)

    builder.set_entry_point("investigator")

    builder.add_edge("investigator", "risk")
    builder.add_edge("risk", "decision")
    builder.add_edge("decision", END)

    return builder.compile()