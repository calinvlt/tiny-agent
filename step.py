from dataclasses import dataclass

@dataclass
class Step:
    """A single step n an agent's trajectory"""

    thought: str = ""
    action: dict|None = None
    observation: str|None = None
    answer: str|None = None
    metadata: dict|None = None

    