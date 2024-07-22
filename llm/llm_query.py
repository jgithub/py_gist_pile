from typing import List, TypedDict

from json.json_object_or_array import JsonObjectOrArray
from llm.llm_q_and_a import LlmQAndA
from dataclasses import dataclass, field


@dataclass
class LlmQuery:
    prompt: str
    additionalContext: JsonObjectOrArray
    qAndA: List[LlmQAndA]
