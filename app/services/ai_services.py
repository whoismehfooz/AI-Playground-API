import logging
from app.config import client
from app.schemas import (GeneralRequest, GeneralResponse, UsageResponse, StructuredAIResponse)
from openai import (APIConnectionError, APITimeoutError, APIStatusError, RateLimitError)
from app.exceptions.custom_exceptions import (AIServiceConnectionError,AIServiceProviderError,AIServiceRateLimitError,AIServiceTimeoutError)
from app.utils.cost import calculate_cost



logger = logging.getLogger(__name__)

def generate_response(data: GeneralRequest) -> GeneralResponse:                   # This SDK's response factor vary not because of TEMPRATURE but REASONING-EFFORT..

    logger.info(
        "Sending request to AI provider | model=%s",
        data.model
    )

    request = {
    "model": data.model,
    "input": data.prompt
    }


    if data.reasoning_effort is not None:
        request["reasoning"] = {
            "effort" : data.reasoning_effort
        }

    if data.max_output_tokens is not None:
        request["max_output_tokens"] = data.max_output_tokens


    try:
        response = client.responses.create(**request)

    except APITimeoutError as exc:
        logger.error(
            "AI provider request timed out | model=%s",
            data.model
        )
        raise AIServiceTimeoutError() from exc

    except APIConnectionError as exc:
        logger.error(
            "Unable to connect to AI provider | model=%s",
            data.model
        )
        raise AIServiceConnectionError() from exc

    except RateLimitError as exc:
        logger.warning(
                    "AI provider rate limit exceeded | model=%s",
                    data.model
                )
        raise AIServiceRateLimitError() from exc

    except APIStatusError as exc:
        logger.error(
            "AI provider request failed | model=%s",
            data.model
            )
        raise AIServiceProviderError() from exc

    logger.info(
        "AI provider request completed | model=%s",
        response.model
    )

    estimated_cost = calculate_cost(
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens
    )

    return GeneralResponse(
        text= response.output_text,
        model= response.model,
        usage= UsageResponse(
            input_tokens= response.usage.input_tokens,
            output_tokens= response.usage.output_tokens,
            total_tokens= response.usage.total_tokens,
            reasoning_tokens= response.usage.output_tokens_details.reasoning_tokens
        ),
        estimated_cost=estimated_cost
    )


def generate_structured_response(
    data: GeneralRequest,
) -> StructuredAIResponse:

    logger.info(
        "Sending structured request to AI provider | model=%s",
        data.model,
    )

    request = {
        "model": data.model,
        "input": data.prompt,
        "text_format": StructuredAIResponse,
    }

    if data.reasoning_effort is not None:
        request["reasoning"] = {
            "effort": data.reasoning_effort
        }

    if data.max_output_tokens is not None:
        request["max_output_tokens"] = data.max_output_tokens

    try:
        response = client.responses.parse(**request)

    except APITimeoutError as exc:
        logger.error(
            "Structured AI request timed out | model=%s",
            data.model,
        )
        raise AIServiceTimeoutError() from exc

    except APIConnectionError as exc:
        logger.error(
            "Unable to connect to AI provider for structured request | model=%s",
            data.model,
        )
        raise AIServiceConnectionError() from exc

    except RateLimitError as exc:
        logger.warning(
            "AI provider rate limit exceeded for structured request | model=%s",
            data.model,
        )
        raise AIServiceRateLimitError() from exc

    except APIStatusError as exc:
        logger.error(
            "AI provider structured request failed | model=%s",
            data.model,
        )
        raise AIServiceProviderError() from exc

    logger.info(
        "Structured AI request completed | model=%s",
        response.model,
    )

    return response.output_parsed