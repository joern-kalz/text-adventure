"""A text adventure server."""

import getpass
import os
import secrets
from typing import Annotated
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi import HTTPException, Header
from core.gamemaster_system_prompt import get_gamemaster_system_prompt
from adapters.persistence.session_store import get_session, save_session
from adapters.agents.game_overview_agent import invoke_game_overview_agent
from adapters.agents.gamemaster_agent import invoke_gamemaster_agent
from .app import create_app

app = create_app()


class PlayerAction(BaseModel):
    """An action taken by the player character."""

    action: str = Field(description="An action taken by the player character")


@app.post("/start-game")
async def start_game():
    """Starts a new game and returns the initial game state."""
    overview = invoke_game_overview_agent()
    token = secrets.token_urlsafe(32)
    save_session(
        token,
        {"overview": overview, "messages": []},
    )
    return {"token": token} | overview


@app.post("/perform-action")
async def perform_user_message(
    player_action: PlayerAction, x_session_id: Annotated[str, Header()]
):
    """Performs a user action and returns a response from the agent."""

    session = get_session(x_session_id)

    if session is None:
        raise HTTPException(status_code=409, detail="Invalid x-session-id header")

    messages = session["messages"]

    if messages == []:
        messages.append(get_gamemaster_system_prompt(session["overview"]))

    messages = messages + [{"role": "user", "content": player_action.action}]
    result = invoke_gamemaster_agent(messages)
    messages = messages + [{"role": "assistant", "content": result.model_dump_json()}]
    save_session(x_session_id, {"overview": session["overview"], "messages": messages})
    return result


load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
