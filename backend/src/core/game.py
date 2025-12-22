"""A text adventure server."""

import json
import secrets

from src.adapters.model.model import invoke_model
from src.adapters.persistence.session_store import get_session, save_session
from src.core.game_overview_prompt import get_game_overview_prompt
from src.core.gamemaster_system_prompt import get_gamemaster_system_prompt
from src.model.results import (
    CreateGameResult,
    PerformActionResult,
    PerformActionResultSuccess,
)
from src.model.session import Overview


def start_game() -> CreateGameResult:
    """Starts a new game and returns the initial game state."""
    overview = invoke_model(get_game_overview_prompt())
    token = secrets.token_urlsafe(32)
    save_session(
        token,
        {"overview": Overview(**overview), "messages": []},
    )
    return CreateGameResult(token=token, **overview)


def perform_action(action: str, session_id: str) -> PerformActionResult:
    """Performs a user action and returns a response from the agent."""

    session = get_session(session_id)

    if session is None:
        return {"type": "error_session_not_found"}

    messages = session["messages"]

    if messages == []:
        messages.append(get_gamemaster_system_prompt(session["overview"]))

    messages = messages + [{"role": "user", "content": action}]
    result = invoke_model(messages)
    messages = messages + [{"role": "assistant", "content": json.dumps(result)}]
    save_session(session_id, {"overview": session["overview"], "messages": messages})
    return PerformActionResultSuccess(type="success", **result)
