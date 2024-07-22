import unittest
from boolean_util import is_truelike
from llm.llm_query import LlmQuery


class TestLlmQuery(unittest.TestCase):
    def test_anemic(self):
        llm_query = LlmQuery(prompt="hello", additionalContext=None, qAndA=[])


if __name__ == "__main__":
    unittest.main()
