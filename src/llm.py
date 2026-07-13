from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)

from langchain_huggingface import HuggingFacePipeline

from src import config


class HuggingFaceLLM:

    def __init__(self):

        print("=" * 60)
        print("Loading HuggingFace Model...")
        print("=" * 60)

        tokenizer = AutoTokenizer.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
        )

        model = AutoModelForCausalLM.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
            device_map="cpu",
        )

        pipe = pipeline(
            task="text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=config.MAX_NEW_TOKENS,
            temperature=config.TEMPERATURE,
            do_sample=True,
            return_full_text=False,
        )

        self.llm = HuggingFacePipeline(
            pipeline=pipe
        )

    def invoke(self, prompt: str):

        return self.llm.invoke(prompt)


class DummyLLM:

    def invoke(self, prompt: str):

        return f"""
[Financial AI]

Question:
{prompt}

Dummy response.
"""