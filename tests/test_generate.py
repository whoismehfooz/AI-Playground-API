from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate():
    response = client.post(
        "/generate",
        json={
            "prompt":"Say hello in one Short sentance."
        }
    )

    assert response.status_code == 200