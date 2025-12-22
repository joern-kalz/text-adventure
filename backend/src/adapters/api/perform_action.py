"""API endpoint for performing player actions in the game."""

from typing import Annotated

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, Field
from src.core.game import perform_action
from src.model.perform_action_result import PerformActionResultErrorSessionNotFound

router = APIRouter()


class PlayerAction(BaseModel):
    """An action taken by the player character."""

    action: str = Field(description="An action taken by the player character")


class PerformActionResultSuccess(BaseModel):
    """The result of performing a player action successfully."""

    outcome: str = Field(description="Outcome of the performed action")
    quests: list[str] = Field(description="List of current quests")
    inventory: list[str] = Field(description="Items in the player's inventory")
    world: str = Field(description="Description of the current world state")


@router.post("/perform-action")
async def post_perform_action(
    player_action: PlayerAction, x_session_token: Annotated[str, Header()]
):
    """Performs a user action and returns a response from the agent."""
    result = perform_action(player_action.action, x_session_token)
    if isinstance(result, PerformActionResultErrorSessionNotFound):
        raise HTTPException(status_code=404, detail="Session not found")
    else:
        return PerformActionResultSuccess(
            outcome=result.outcome,
            quests=result.quests,
            inventory=result.inventory,
            world=result.world,
        )
