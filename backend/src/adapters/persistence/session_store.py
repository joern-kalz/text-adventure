"""Session persistence for text adventure game sessions."""

from src.model.session import Session

_sessions: dict[str, Session] = {}


def get_session(session_id: str) -> Session | None:
    """Retrieves a session by its ID."""
    return _sessions.get(session_id)


def save_session(session_id: str, session: Session) -> None:
    """Saves a session by its ID."""
    _sessions[session_id] = session
