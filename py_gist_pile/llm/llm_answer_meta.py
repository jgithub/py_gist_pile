from dataclasses import dataclass
from typing import Optional

@dataclass
class LlmAnswerMeta():
    score: Optional[float] = None  # A confidence score - number between 0 and 1
