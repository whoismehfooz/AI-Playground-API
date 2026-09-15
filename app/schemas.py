from pydantic import BaseModel, Field
from typing import Literal



class GeneralRequest(BaseModel):
    prompt : str = Field(min_length=1)
    model : str = "gpt-5.6-luna"
    reasoning_effort :  Literal[
        "low",
        "high",
        "medium",
        "high",
        "xhigh",
        "max"
        ] | None = None
    max_output_tokens : int | None = Field(default=None,ge=1)



class UsageResponse(BaseModel):
    input_tokens : int
    output_tokens : int
    total_tokens : int
    reasoning_tokens : int

class GeneralResponse(BaseModel):
    text : str
    model : str
    usage : UsageResponse
    estimated_cost : float


class StructuredAIResponse(BaseModel):
    answer : str
    summary : str