from agents.investigator import investigator_agent
from agents.risk_analyzer import risk_analyzer_agent
from agents.decision_agent import decision_agent
from observability.logger import PipelineLogger
from graph.langgraph_pipeline import build_graph

import time

graph = build_graph()


def run_pipeline(alert_id: str):

    logger = PipelineLogger()
    start = time.time()
    
    result = graph.invoke({
        "alert_id": alert_id,
        "logger": logger
    })

    return {
        "alert_id": alert_id,
        "context": result.get("context"), 
        "analysis": result.get("analysis"),
        "decision": result.get("decision"),
        "audit_trail": logger.get_logs(),
        "metadata": {
            "latency_ms": (time.time() - start) * 1000,
        },
    }