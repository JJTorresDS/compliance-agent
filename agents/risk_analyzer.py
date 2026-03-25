def risk_analyzer_agent(context: dict):
    transactions = context["transactions"]

    total = sum(t["amount"] for t in transactions)

    risk_score = min(10, total / 100)

    anomalies = []
    if any(t["country"] != "AR" for t in transactions):
        anomalies.append("Foreign transactions detected")

    return {
        "risk_score": risk_score,
        "anomalies": anomalies,
        "summary": f"Total volume: {total}"
    }