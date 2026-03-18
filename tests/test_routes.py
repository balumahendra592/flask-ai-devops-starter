import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["status"] == "ok"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "healthy"

def test_ai_ask_missing_prompt(client):
    res = client.post("/ai/ask", json={})
    assert res.status_code == 400
    assert "error" in res.json
