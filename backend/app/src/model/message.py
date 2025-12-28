"""Message domain model for the text adventure game."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Message:
    """A message in the game."""

    role: Literal["system", "user", "assistant"]
    content: str
