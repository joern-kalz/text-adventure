"""PerformActionResult domain model for the text adventure game."""

from dataclasses import dataclass


@dataclass
class PerformActionResultSuccess:
    """The result of performing a player action successfully."""

    outcome: str
    quests: list[str]
    inventory: list[str]
    world: str


@dataclass
class PerformActionResultErrorSessionNotFound:
    """The result of performing a player action with an invalid session token."""


PerformActionResult = (
    PerformActionResultSuccess | PerformActionResultErrorSessionNotFound
)
