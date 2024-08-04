import unittest
from py_gist_pile.llm.llm_query import LlmQuery
import json


class TestLlmQuery(unittest.TestCase):
    def test_anemic(self):
        llm_query = LlmQuery(prompt="hello", additional_context=None, q_and_a=[])
        self.assertEqual(llm_query.prompt, "hello")

    def test_can_be_json_serialized(self):
        llm_query = LlmQuery(prompt="hello", additional_context=None, q_and_a=[])
        # llm_query = LlmQuery(prompt="Hey Gemini...", 
        #                      additional_context=None, 
        #                      q_and_a=[
        #                         LlmQAndA(question="What color is the sky on Earth when it's clear?", answer=None, answer_meta=None)
        #                     ]        
        self.assertEqual(json.dumps(llm_query, default=vars), "hello")

if __name__ == "__main__":
    unittest.main()
