from typing import List

from jjson.json_object_or_array import JsonObjectOrArray
from llm_q_and_a import LlmQAndA
from dataclasses import dataclass

@dataclass
class LlmQuery:
    '''
    Anemic LlmQuery model
    '''
    prompt: str
    additionalContext: JsonObjectOrArray
    qAndA: List[LlmQAndA]
