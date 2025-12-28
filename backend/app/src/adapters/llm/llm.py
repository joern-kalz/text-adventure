"""Agent to generate a game overview."""

import json
from dataclasses import asdict
from typing import cast

from langchain_groq import ChatGroq
from src.model.message import Message


def invoke_llm(prompt: str | list[Message]) -> dict:
    """Invokes the agent to get a game overview."""
    model = ChatGroq(model="llama-3.1-8b-instant")
    response = model.invoke(convert_prompt(prompt))
    return json.loads(cast(str, response.content))


def convert_prompt(prompt: str | list[Message]):
    """Converts the prompt to the format required by the LLM"""
    if isinstance(prompt, list):
        return [asdict(m) for m in prompt]
    return prompt
