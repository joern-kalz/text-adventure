"""Domain model for the text adventure game."""

from typing import Literal, TypedDict


class Overview(TypedDict):
    """Overview of the game."""

    setting: str
    beginning: str
    goal: str


class Message(TypedDict):
    """A message in the game."""

    role: Literal["system"] | Literal["user"] | Literal["assistant"]
    content: str


class Session(TypedDict):
    """A game session."""

    overview: Overview
    messages: list[Message]
