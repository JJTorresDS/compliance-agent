from agents.investigator import investigator_agent


def test_investigator_returns_context():
    result = investigator_agent("123")

    assert "user" in result
    assert "transactions" in result
    assert "documents" in result

    assert isinstance(result["transactions"], list)
    assert isinstance(result["documents"], list)