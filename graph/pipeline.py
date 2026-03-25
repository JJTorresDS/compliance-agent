from agents.investigator import investigator_agent
from agents.risk_analyzer import risk_analyzer_agent
from agents.decision_agent import decision_agent
from observability.logger import PipelineLogger
import time

def run_pipeline(alert_id: str):

    logger = PipelineLogger()
    start = time.time()

    context = investigator_agent(alert_id)
    logger.log("investigator",alert_id, context)

    analysis = risk_analyzer_agent(context)
    logger.log("risk_analyzer",context, analysis)

    decision = decision_agent(analysis)
    logger.log("decision", analysis, decision)

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