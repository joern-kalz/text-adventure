"""Session persistence for text adventure game sessions."""

import os
from dataclasses import asdict
import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

from src.model.message import Message
from src.model.overview import Overview
from src.model.session import Session

_sessions: dict[str, Session] = {}
_table_name = os.environ.get("SESSIONS_TABLE_NAME")

def read_session(session_token: str) -> Session | None:
    """Retrieves a session by its token."""
    if _table_name:
        response = boto3.client("dynamodb").get_item(
            TableName=_table_name, Key={"session_token": {"S": session_token}}
        )
        item = response.get("Item")
        if not item:
            return None
        deserializer = TypeDeserializer()
        deserialized = {k: deserializer.deserialize(v) for k, v in item.items()}
        return Session(
            overview=Overview(**deserialized["overview"]),
            messages=[Message(**m) for m in deserialized["messages"]],
        )
    return _sessions.get(session_token)


def write_session(session_token: str, session: Session) -> None:
    """Saves a session by its token."""
    if _table_name:
        item = asdict(session)
        item["session_token"] = session_token
        serializer = TypeSerializer()
        serialized = {k: serializer.serialize(v) for k, v in item.items()}
        boto3.client("dynamodb").put_item(TableName=_table_name, Item=serialized)
    else:
        _sessions[session_token] = session
