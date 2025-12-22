"""Domain model for the text adventure game using dataclasses."""

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Overview:
    """Overview of the game."""

    setting: str
    beginning: str
    goal: str


@dataclass
class Message:
    """A message in the game."""

    role: Literal["system", "user", "assistant"]
    content: str


@dataclass
class Session:
    """A game session."""

    overview: Overview
    messages: list[Message] = field(default_factory=list)
