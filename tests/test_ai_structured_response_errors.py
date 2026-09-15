import pytest
import httpx
from unittest.mock import patch

from app.schemas import GeneralRequest
from app.services.ai_services import generate_structured_response


from app.exceptions.custom_exceptions import (
                                            AIServiceRateLimitError,
                                            AIServiceConnectionError,
                                            AIServiceTimeoutError,
                                            AIServiceProviderError
)
from openai import (
                    APIConnectionError,
                    APIStatusError,
                    APITimeoutError,
                    RateLimitError
)


general_request = GeneralRequest(
        prompt="Explain what an API is."
)

def test_structrued_response_maps_timeout():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses"
    )

    provider_error = APITimeoutError(request=http_request)

    with patch(
        "app.services.ai_services.client.responses.parse",
        side_effect=provider_error
    ):
        with pytest.raises(AIServiceTimeoutError):
            generate_structured_response(general_request)


def test_structured_response_maps_rate_limit():
    http_request = httpx.Request(
        "POST",
        "https://api.oepenai.com/v1/responses"
    )

    http_response = httpx.Response(
        429,
        request=http_request
    )

    provider_error = RateLimitError(
        message="Rate Limit Exceeded.",
        response=http_response,
        body=None
    )

    with patch(
        "app.services.ai_services.client.responses.parse",
        side_effect=provider_error
    ):
        with pytest.raises(AIServiceRateLimitError):
            generate_structured_response(general_request)


def test_structured_response_maps_connection_error():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses"
    )

    provider_error = APIConnectionError(request=http_request)

    with patch(
        "app.services.ai_services.client.responses.parse",
        side_effect=provider_error
    ):
        with pytest.raises(AIServiceConnectionError):
            generate_structured_response(general_request)


def test_structured_response_maps_provider_error():
    provider_error = APIStatusError(
        "Provider request failed.",
        response=httpx.Response(
            500,
            request=httpx.Request(
                "POST",
                "https://api.openai.com/v1/responses"
            )
        ),
        body=None
    )

    with patch(
        "app.services.ai_services.client.responses.parse",
        side_effect=provider_error
    ):
        with pytest.raises(AIServiceProviderError):
            generate_structured_response(general_request)