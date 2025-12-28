"""Session persistence for text adventure game sessions."""

from src.model.session import Session

_sessions: dict[str, Session] = {}


def get_session(session_token: str) -> Session | None:
    """Retrieves a session by its token."""
    return _sessions.get(session_token)


def save_session(session_token: str, session: Session) -> None:
    """Saves a session by its token."""
    _sessions[session_token] = session
