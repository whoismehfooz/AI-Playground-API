from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app
from app.exceptions.custom_exceptions import (
                                            AIServiceTimeoutError,
                                            AIServiceRateLimitError,
                                            AIServiceConnectionError,
                                            AIServiceProviderError)


client = TestClient(app)


def test_ai_timeout_handler():
    with patch(
        "app.main.generate_response",
        side_effect=AIServiceTimeoutError()
    ):
        response = client.post(
            "/generate",
            json={
                "prompt":"test_timeout"
            }
        )

        assert response.status_code == 504
        assert response.json() == {
            "detail": "AI provider request timed out."

        }


def test_ai_rate_limit_handler():
    with patch(
        "app.main.generate_response",
        side_effect=AIServiceRateLimitError
    ):
        response = client.post(
            "/generate",
            json={
                "prompt":"test_rate_limit"
            }
        )

        assert response.status_code == 429
        assert response.json() == {
            "detail":"AI provider rate limit exceeded."
        }


def test_ai_connection_handler():
    with patch(
        "app.main.generate_response",
        side_effect=AIServiceConnectionError
    ):
        response = client.post(
            "/generate",
            json={
                "prompt":"test_connection"
            }
        )

        assert response.status_code == 502
        assert response.json() == {
            "detail":"Unable to connect with AI provider."
        }

def test_ai_provider_handler():
    with patch(
        "app.main.generate_response",
        side_effect=AIServiceProviderError
    ):
        response = client.post(
            "/generate",
            json={
                "prompt":"test_provider"
            }
        )

        assert response.status_code == 502
        assert response.json() == {
            "detail":"AI provider request failed."
        }