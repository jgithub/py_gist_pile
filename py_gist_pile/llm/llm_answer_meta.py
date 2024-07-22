from typing import TypedDict


class LlmAnswerMeta(TypedDict):
    score: float  # A confidence score - number between 0 and 1
