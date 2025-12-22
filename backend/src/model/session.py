"""Session domain model for the text adventure game."""

from dataclasses import dataclass, field

from src.model.message import Message
from src.model.overview import Overview


@dataclass
class Session:
    """A game session."""

    overview: Overview
    messages: list[Message] = field(default_factory=list)
