from tools.mock_db import get_transactions, get_user_profile
from tools.mock_storage import get_documents


def investigator_agent(alert_id: str):
    user_id = f"user_{alert_id}"

    transactions = get_transactions(user_id)
    profile = get_user_profile(user_id)
    documents = get_documents(user_id)

    return {
        "user": profile,
        "transactions": transactions,
        "documents": documents,
    }