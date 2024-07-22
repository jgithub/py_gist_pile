from abc import ABC, abstractmethod
from py_gist_pile.llm.llm_query import LlmQuery
from py_gist_pile.llm.llm_response import LlmResponse

class LlmConversationService(ABC):
    @abstractmethod
    async def ask_query(self, llm_query: LlmQuery) -> LlmResponse:
        """
        Abstract method to ask a query.

        :param llm_query: The query to ask
        :return: A Future that will resolve to an LlmResponse
        """
        pass