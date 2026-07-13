import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from src import config


class LLMService:

    def __init__(self):

        print("Loading tokenizer...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
        )

        print("Loading model...")

        self.model = AutoModelForCausalLM.from_pretrained(
            config.MODEL_NAME,
            token=config.HF_TOKEN,
            device_map="cpu",
            torch_dtype=torch.float32,
        )

    def invoke(self, prompt: str):

        messages = [
            {
                "role": "system",
                "content": "You are a professional financial advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
        )

        with torch.no_grad():

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=128,
                do_sample=True,
                temperature=0.3,
                top_p=0.9,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        generated = outputs[0][inputs.input_ids.shape[1]:]

        return self.tokenizer.decode(
            generated,
            skip_special_tokens=True,
        )