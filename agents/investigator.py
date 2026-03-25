from tools.mock_db import get_transactions, get_user_profile
from tools.mock_storage import get_documents


def investigator_agent(alert_id: str):
    """
    Dado un ID de alerta, busca en BigQuery el historial de
    transacciones del cliente (últimos 90 días), extrae los documentos PDF relevantes de
    GCS, y construye un contexto estructurado del caso.

    Args:
        alert_id: ID de la alerta

    Returns:
        Contexto estructurado del caso
    """
    user_id = f"user_{alert_id}"

    transactions = get_transactions(user_id)
    profile = get_user_profile(user_id)
    documents = get_documents(user_id)

    return {
        "user": profile,
        "transactions": transactions,
        "documents": documents,
    }