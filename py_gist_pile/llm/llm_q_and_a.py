from dataclasses import dataclass
from py_gist_pile.llm.llm_answer_meta import LlmAnswerMeta

# class LlmQAndA(TypedDict):
#     question: str   # This is populated in the query
#     answer: str     # Additionally, these are populated in the response
#     answerMeta: LlmAnswerMeta


@dataclass
class LlmQAndA:
    question: str  # This is populated in the query
    answer: str  # Additionally, these are populated in the response
    answerMeta: LlmAnswerMeta
