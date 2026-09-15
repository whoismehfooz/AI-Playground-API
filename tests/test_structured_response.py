from unittest.mock import patch

from app.schemas import GeneralRequest, StructuredAIResponse
from app.services.ai_services import generate_structured_response




def test_generate_structured_response():
    request = GeneralRequest(
        prompt="Explain what an API is.",
        reasoning_effort="low",
        max_output_tokens=100
    )

    expected_response = StructuredAIResponse(
        answer="An API allows software systems to communicate.",
        summary="API enables software interactions."
    )

    fake_response = type(
        "FakeResponse",
        (),
        {
            "output_parsed": expected_response,
            "model":"gpt-5.6-luna"
        },
    )()

    with patch(
        "app.services.ai_services.client.responses.parse",
        return_value=fake_response
    )as mock_parse:

        result = generate_structured_response(request)

        assert result == expected_response

        sent_request = mock_parse.call_args.kwargs

        assert sent_request["model"] == "gpt-5.6-luna"
        assert sent_request["input"] == "Explain what an API is."
        assert sent_request["text_format"] is StructuredAIResponse
        assert sent_request["reasoning"]["effort"] == "low"
        assert sent_request["max_output_tokens"] == 100