import pytest

from unittest.mock import patch

from app.schemas import GeneralRequest

from app.services.ai_services import generate_response

from app.utils.cost import calculate_cost


def test_generate_response_sends_max_output_tokens():
    request = GeneralRequest(
        prompt="test max output tokens",
        max_output_tokens=50,
    )

    fake_response = type(
        "FakeResponse",
        (),
        {
            "output_text": "test response",
            "model": "gpt-5.6-luna",
            "usage": type(
                "FakeUsage",
                (),
                {
                    "input_tokens": 10,
                    "output_tokens": 5,
                    "total_tokens": 15,
                    "output_tokens_details": type(
                        "FakeOutputDetails",
                        (),
                        {"reasoning_tokens": 0},
                    )(),
                },
            )(),
        },
    )()

    with patch(
        "app.services.ai_services.client.responses.create",
        return_value=fake_response,
    ) as mock_create:
        result = generate_response(request)

        mock_create.assert_called_once()

        sent_request = mock_create.call_args.kwargs

        assert sent_request["max_output_tokens"] == 50

        assert result.estimated_cost == pytest.approx(
            calculate_cost(
                input_tokens=fake_response.usage.input_tokens,
                output_tokens=fake_response.usage.output_tokens,
            )
        )

        assert result.estimated_cost == pytest.approx(0.000008)