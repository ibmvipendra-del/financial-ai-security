import sys
from pathlib import Path

# Add project root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from huggingface_hub import InferenceClient
from src import config

print("=" * 60)
print("Testing Hugging Face Connection")
print("=" * 60)

client = InferenceClient(
    api_key=config.HF_TOKEN
)

response = client.chat.completions.create(
    model="HuggingFaceH4/zephyr-7b-beta",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
    max_tokens=50
)

print("\nModel Response:\n")
print(response.choices[0].message.content)