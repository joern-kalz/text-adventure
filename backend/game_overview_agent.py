""" "Agent to generate a game overview."""

from typing import cast
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dto import Overview


class GameOverviewResponse(BaseModel):
    """Overview of the game"""

    setting: str = Field(
        description="Description of an imaginative game setting in a few words like ancient Greece"
    )
    beginning: str = Field(
        description="Description of the location where the player starts in 2-3 sentences"
    )
    goal: str = Field(
        description="Description of the goal the player must reach to succeed in the game"
    )


def invoke_game_overview_agent() -> Overview:
    """Invokes the agent to get a game overview."""
    unstructured_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    model = unstructured_model.with_structured_output(GameOverviewResponse)
    response = model.invoke("Generate an overview for a text adventure game.")
    overview = cast(GameOverviewResponse, response)

    return Overview(
        setting=overview.setting,
        beginning=overview.beginning,
        goal=overview.goal,
    )
