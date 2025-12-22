"""API endpoint for starting a new game."""

from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.core.game import start_game

router = APIRouter()


class StartGameResponse(BaseModel):
    """Response for starting a new game."""

    token: str = Field(description="Secret session token for the game")
    setting: str = Field(description="Setting of the game")
    beginning: str = Field(description="Beginning of the game")
    goal: str = Field(description="Goal of the game")


@router.post("/start-game")
async def post_start_game() -> StartGameResponse:
    """Starts a new game and returns the initial game state."""
    result = start_game()
    return StartGameResponse(
        token=result.token,
        setting=result.overview.setting,
        beginning=result.overview.beginning,
        goal=result.overview.goal,
    )
