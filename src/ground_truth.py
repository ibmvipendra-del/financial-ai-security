from dataclasses import dataclass, field


@dataclass
class GroundTruth:

    tool: str

    values: dict = field(default_factory=dict)

    text: str = ""