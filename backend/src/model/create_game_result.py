"""CreateGameResult domain model for the text adventure game."""

from dataclasses import dataclass

from src.model.overview import Overview


@dataclass
class CreateGameResult:
    """Result of creating a new game."""

    token: str
    overview: Overview
