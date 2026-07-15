from src.llm import DummyLLM
from src.llm import HuggingFaceLLM


USE_REAL_MODEL = True


class LLMFactory:

    @staticmethod
    def create():

        if USE_REAL_MODEL:

            return HuggingFaceLLM()

        return DummyLLM()
    


    