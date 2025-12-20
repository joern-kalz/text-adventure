"""Agent to get the result of a player action."""

from typing import cast
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


class PlayerActionResult(BaseModel):
    """The result of a player action."""

    outcome: str = Field(
        description="Description of the outcome of the action in 3-5 sentences"
    )
    quests: list[str] = Field(
        description="List of current quests the player is undertaking"
    )
    inventory: list[str] = Field(
        description="List of all items the player is currently carrying"
    )
    world: str = Field(
        description="Detailed description of the current state of the whole game world"
    )


def invoke_gamemaster_agent(messages: list) -> PlayerActionResult:
    """Invokes the gamemaster agent to get a response to a player action."""
    unstructured_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    model = unstructured_model.with_structured_output(PlayerActionResult)
    response = model.invoke(messages)
    return cast(PlayerActionResult, response)
