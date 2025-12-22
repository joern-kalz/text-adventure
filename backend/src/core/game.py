"""A text adventure server using dataclass models."""

import json
import secrets

from src.adapters.llm.llm import invoke_llm
from src.adapters.persistence.session_store import get_session, save_session
from src.core.game_overview_prompt import get_game_overview_prompt
from src.core.gamemaster_system_prompt import get_gamemaster_system_prompt
from src.model.results import (
    CreateGameResult,
    PerformActionResult,
    PerformActionResultErrorSessionNotFound,
    PerformActionResultSuccess,
)
from src.model.session import Message, Overview, Session


def start_game() -> CreateGameResult:
    """Starts a new game and returns the initial game state."""
    overview_dict = invoke_llm(get_game_overview_prompt())
    overview = Overview(**overview_dict)
    token = secrets.token_urlsafe(32)
    save_session(token, Session(overview=overview, messages=[]))
    return CreateGameResult(token=token, overview=overview)


def perform_action(action: str, session_id: str) -> PerformActionResult:
    """Performs a user action and returns a response from the agent."""

    session = get_session(session_id)

    if session is None:
        return PerformActionResultErrorSessionNotFound()

    messages = session.messages

    if messages == []:
        messages.append(get_gamemaster_system_prompt(session.overview))

    messages = messages + [Message(role="user", content=action)]
    result = invoke_llm(messages)
    messages = messages + [Message(role="assistant", content=json.dumps(result))]
    save_session(session_id, Session(overview=session.overview, messages=messages))

    return PerformActionResultSuccess(
        outcome=result["outcome"],
        quests=result["quests"],
        inventory=result["inventory"],
        world=result["world"],
    )
