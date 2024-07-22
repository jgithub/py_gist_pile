from typing import List, Optional
from dataclasses import dataclass

from jjson.json_object_or_array import JsonObjectOrArray
from llm.llm_q_and_a import LlmQAndA

@dataclass
class LlmResponse:
    rootResponseText: Optional[str] = None
    rootResponseJson: Optional[JsonObjectOrArray] = None
    qAndA: Optional[List[LlmQAndA]] = None