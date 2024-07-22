from typing import List, Optional
from dataclasses import dataclass

from py_gist_pile.jjson.json_object_or_array import JsonObjectOrArray
from py_gist_pile.llm.llm_q_and_a import LlmQAndA

@dataclass
class LlmResponse:
    rootResponseText: Optional[str] = None
    rootResponseJson: Optional[JsonObjectOrArray] = None
    qAndA: Optional[List[LlmQAndA]] = None