from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_endpoint_structure():
    response = client.get("/analyze/123")

    assert response.status_code == 200

    data = response.json()

    assert "alert_id" in data
    assert "analysis" in data
    assert "decision" in data

    assert isinstance(data["analysis"], dict)
    assert isinstance(data["decision"], dict)