import pytest
import httpx
from unittest.mock import patch

from app.schemas import GeneralRequest
from app.services.ai_services import generate_response

from app.exceptions.custom_exceptions import (
                                            AIServiceConnectionError,
                                            AIServiceRateLimitError,
                                            AIServiceProviderError,
                                            AIServiceTimeoutError,
)

from openai import (
                    APITimeoutError,
                    RateLimitError,
                    APIConnectionError,
                    APIStatusError)


general_request = GeneralRequest(
    prompt="test error handling"
)


def test_generate_response_maps_timeout():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses"
    )

    provider_error = APITimeoutError(request=http_request,)


    with patch(
        "app.services.ai_services.client.responses.create",
        side_effect=provider_error
    ):

        with pytest.raises(AIServiceTimeoutError):
            generate_response(general_request)


def test_generate_response_maps_rate_limit():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses"
    )

    http_response = httpx.Response(
        429,
        request=http_request,
    )

    provider_error = RateLimitError(
        message="Rate Limit Exceeded.",
        response=http_response,
        body=None
    )
    with patch(
        "app.services.ai_services.client.responses.create",
        side_effect=provider_error
    ):
        with pytest.raises(AIServiceRateLimitError):
            generate_response(general_request)


def test_generate_response_maps_connection_error():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses",
    )

    provider_error = APIConnectionError(
        message="Connection failed",
        request=http_request)

    with patch(
        "app.services.ai_services.client.responses.create",
        side_effect=provider_error,
    ):
        with pytest.raises(AIServiceConnectionError):
            generate_response(general_request)


def test_generate_response_maps_provider_error():
    http_request = httpx.Request(
        "POST",
        "https://api.openai.com/v1/responses",
    )

    http_response = httpx.Response(
        500,
        request=http_request,
    )

    provider_error = APIStatusError(
        "Provider failure",
        response=http_response,
        body=None,
    )

    with patch(
        "app.services.ai_services.client.responses.create",
        side_effect=provider_error,
    ):
        with pytest.raises(AIServiceProviderError):
            generate_response(general_request)