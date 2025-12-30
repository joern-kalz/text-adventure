"""A text adventure server using dataclass models."""

import json
import secrets

from src.adapters.llm.llm import invoke_llm
from src.adapters.persistence.session_store import read_session, write_session
from src.core.game_overview_prompt import get_game_overview_prompt
from src.core.gamemaster_system_prompt import get_gamemaster_system_prompt
from src.model.create_game_result import CreateGameResult
from src.model.message import Message
from src.model.overview import Overview
from src.model.perform_action_result import (
    PerformActionResult,
    PerformActionResultErrorSessionNotFound,
    PerformActionResultSuccess,
)
from src.model.session import Session


def start_game() -> CreateGameResult:
    """Starts a new game and returns the initial game state."""
    overview_dict = invoke_llm(get_game_overview_prompt())
    overview = Overview(**overview_dict)
    token = secrets.token_urlsafe(32)
    system_prompt = get_gamemaster_system_prompt(overview)
    write_session(token, Session(overview=overview, messages=[system_prompt]))
    return CreateGameResult(session_token=token, overview=overview)


def perform_action(action: str, session_token: str) -> PerformActionResult:
    """Performs a user action and returns a response from the agent."""

    session = read_session(session_token)

    if session is None:
        return PerformActionResultErrorSessionNotFound()

    messages = session.messages
    messages.append(Message(role="user", content=action))
    result = invoke_llm(messages)
    messages.append(Message(role="assistant", content=json.dumps(result)))
    write_session(session_token, session)

    return PerformActionResultSuccess(
        outcome=result["outcome"],
        quests=result["quests"],
        inventory=result["inventory"],
        world=result["world"],
    )
