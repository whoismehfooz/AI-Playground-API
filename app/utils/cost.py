INPUT_PRICE_PER_MILLION = 0.20
OUTPUT_PRICE_PER_MILLION = 1.20


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
) -> float:
    input_cost = (
        input_tokens / 1_000_000
    ) * INPUT_PRICE_PER_MILLION

    output_cost = (
        output_tokens / 1_000_000
    ) * OUTPUT_PRICE_PER_MILLION

    return input_cost + output_cost