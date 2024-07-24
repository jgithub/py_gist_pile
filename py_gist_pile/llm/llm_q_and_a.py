from dataclasses import dataclass
from typing import Optional
from py_gist_pile.llm.llm_answer_meta import LlmAnswerMeta

# class LlmQAndA(TypedDict):
#     question: str   # This is populated in the query
#     answer: str     # Additionally, these are populated in the response
#     answer_meta: LlmAnswerMeta


@dataclass
class LlmQAndA:
    question: str  # This is populated in the query
    answer: Optional[str] = None  # Additionally, these are populated in the response
    answer_meta: Optional[LlmAnswerMeta] = None
