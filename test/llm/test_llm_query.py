import unittest
from llm.llm_query import LlmQuery


class TestLlmQuery(unittest.TestCase):
    def test_anemic(self):
        llm_query = LlmQuery(prompt="hello", additionalContext=None, qAndA=[])
        self.assertEqual(llm_query.prompt, "hello")

if __name__ == "__main__":
    unittest.main()
