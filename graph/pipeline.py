from agents.investigator import investigator_agent, risk_analyzer_agent, decision_agent
from observability.logger import PipelineLogger
import time

def run_pipeline(alert_id: str):

    logger = PipelineLogger()
    start = time.time()

    context = investigator_agent(alert_id)
    logger.log("investigator", context)

    analysis = risk_analyzer_agent(context)
    logger.log("risk_analyzer", analysis)

    decision = decision_agent(analysis)
    logger.log("decision", decision)

    return {
        "alert_id": alert_id,
        "context": context, 
        "analysis": analysis,
        "decision": decision,
        "audit_trail": logger.get_logs(),
        "metadata": {
            "latency_ms": (time.time() - start) * 1000,
        },
    }