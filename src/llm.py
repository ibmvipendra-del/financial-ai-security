import time

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)

from src import config


class HuggingFaceLLM:

    def __init__(self):

        print("=" * 60)
        print("Loading HuggingFace Model...")
        print("=" * 60)

        self.tokenizer = AutoTokenizer.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
            device_map="cpu",
            torch_dtype="auto",
        )

        self.pipe = pipeline(
            task="text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )

    def invoke(self, question: str):

        messages = [

            {
                "role": "system",
                "content": (
                    "You are a helpful financial advisor. "
                    "Answer accurately and briefly."
                ),
            },

            {
                "role": "user",
                "content": question,
            },

        ]

        prompt = self.tokenizer.apply_chat_template(

            messages,

            tokenize=False,

            add_generation_prompt=True,

        )

        start = time.time()

        response = self.pipe(

            prompt,

            max_new_tokens=config.MAX_NEW_TOKENS,

            do_sample=False,

            return_full_text=False,

            clean_up_tokenization_spaces=False,

        )

        elapsed = time.time() - start

        print(f"LLM Time: {elapsed:.2f} seconds")

        return response[0]["generated_text"].strip()


class DummyLLM:

    def invoke(self, question: str):

        return f"""
[Financial AI]

Question:
{question}

Dummy response.
"""