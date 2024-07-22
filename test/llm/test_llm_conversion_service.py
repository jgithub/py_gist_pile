import unittest
from llm_query import LlmQuery
from py_gist_pile.log.get_logger import get_logger
from py_gist_pile.llm.llm_conversation_service import LlmConversationService
from llm_response import LlmResponse


class TestLlmConversionService(unittest.TestCase):
    async def test_imports(self):
        llmConversationService: LlmConversationService = FakeiLlmConversationServiceImpl()
        llm_query = LlmQuery(prompt="hello", additionalContext=None, qAndA=[])
        self.assertEqual(llm_query.prompt, "hello")
        response = await llmConversationService.ask_query(LlmQuery())
        self.assertEqual(response.rootResponseText, "hello")

if __name__ == "__main__":
    unittest.main()


LOG = get_logger("FakeiLlmConversationServiceImpl")

class FakeiLlmConversationServiceImpl(LlmConversationService):
    async def ask_query(self, llm_query: LlmQuery) -> LlmResponse:
      print("Hello")
      return LlmResponse(rootResponseText="hello")