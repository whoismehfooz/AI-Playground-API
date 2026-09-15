from app.main import app

from fastapi.testclient import TestClient


client = TestClient(app)


def test_generate_rejects_empty_prompts():
    response = client.post(
        "/generate/structured",
        json={
            "prompt":""
        }
    )

    assert response.status_code == 422


def test_generate_rejects_invalid_reasoning():
    response = client.post(
        "/generate/structured",
        json={
            "prompt":"Explain APIs",
            "reasoning_effort":"invalid"
        }
    )

    assert response.status_code == 422

def test_generate_rejects_invalid_max_output_tokens():
    response = client.post(
        "/generate/structured",
        json={
            "prompt":"Explain APIs",
            "max_output_tokens":0
        }
    )
    assert response.status_code == 422