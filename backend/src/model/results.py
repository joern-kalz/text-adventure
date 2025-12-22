"""Domain model for the text adventure game using dataclasses."""

from dataclasses import dataclass

from src.model.overview import Overview


@dataclass
class CreateGameResult:
    """Result of creating a new game."""

    token: str
    overview: Overview


@dataclass
class PerformActionResultSuccess:
    """The result of performing a player action successfully."""

    outcome: str
    quests: list[str]
    inventory: list[str]
    world: str


@dataclass
class PerformActionResultErrorSessionNotFound:
    """The result of performing a player action with an invalid session ID."""


PerformActionResult = (
    PerformActionResultSuccess | PerformActionResultErrorSessionNotFound
)
