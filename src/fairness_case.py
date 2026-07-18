from dataclasses import dataclass


@dataclass
class FairnessCase:

    attribute: str

    value_a: str

    value_b: str

    prompt_a: str

    prompt_b: str