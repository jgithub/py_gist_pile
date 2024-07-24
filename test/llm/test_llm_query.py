import unittest
from py_gist_pile.llm.llm_query import LlmQuery


class TestLlmQuery(unittest.TestCase):
    def test_anemic(self):
        llm_query = LlmQuery(prompt="hello", additional_context=None, q_and_a=[])
        self.assertEqual(llm_query.prompt, "hello")

if __name__ == "__main__":
    unittest.main()
