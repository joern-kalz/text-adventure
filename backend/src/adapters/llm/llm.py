"""Agent to generate a game overview."""

import json
from typing import cast

from langchain_groq import ChatGroq


def invoke_llm(prompt: str | list) -> dict:
    """Invokes the agent to get a game overview."""
    model = ChatGroq(model="llama-3.1-8b-instant")
    response = model.invoke(prompt)
    return json.loads(cast(str, response.content))
