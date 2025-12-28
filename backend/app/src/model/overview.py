"""Overview domain model for the text adventure game."""

from dataclasses import dataclass


@dataclass
class Overview:
    """Overview of the game."""

    setting: str
    beginning: str
    goal: str
