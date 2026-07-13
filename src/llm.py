from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        pass


class DummyLLM(BaseLLM):

    def invoke(self, prompt: str) -> str:

        return (
            f"[Dummy LLM]\n"
            f"I received your question:\n\n"
            f"{prompt}\n\n"
            f"The real LLM will replace me in the next step."
        )