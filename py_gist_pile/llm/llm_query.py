from typing import List

from py_gist_pile.jjson.json_object_or_array import JsonObjectOrArray
from py_gist_pile.llm.llm_q_and_a import LlmQAndA
from dataclasses import dataclass

@dataclass
class LlmQuery:
    '''
    Anemic LlmQuery model
    '''
    prompt: str
    additional_context: JsonObjectOrArray
    q_and_a: List[LlmQAndA]
