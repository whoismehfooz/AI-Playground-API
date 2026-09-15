import pytest
from app.utils.cost import calculate_cost

def test_calculate_cost():
    cost = calculate_cost(
        input_tokens=1_000,
        output_tokens=500,
    )

    assert cost == pytest.approx(0.0008)