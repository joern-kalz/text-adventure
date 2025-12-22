"""Domain model for the text adventure game."""

from typing import Literal, TypedDict


class CreateGameResult(TypedDict):
    """Result of creating a new game."""

    token: str
    setting: str
    beginning: str
    goal: str


class PerformActionResultSuccess(TypedDict):
    """The result of performing a player action successfully."""

    type: Literal["success"]
    outcome: str
    quests: list[str]
    inventory: list[str]
    world: str


class PerformActionResultErrorSessionNotFound(TypedDict):
    """The result of performing a player action with an invalid session ID."""

    type: Literal["error_session_not_found"]


PerformActionResult = (
    PerformActionResultSuccess | PerformActionResultErrorSessionNotFound
)
