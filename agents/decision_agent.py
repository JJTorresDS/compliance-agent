def decision_agent(analysis: dict):
    score = analysis["risk_score"]

    if score > 7:
        decision = "ESCALATE"
    elif score > 3:
        decision = "REVIEW"
    else:
        decision = "DISMISS"

    return {
        "decision": decision,
        "confidence": round(score / 10, 2),
        "reasoning": f"Based on score {score}"
    }