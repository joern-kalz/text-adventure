"""Mocks for ChatGroq interactions in tests."""

import json
from types import SimpleNamespace

import pytest_mock


def mock_chatgroq(mocker: pytest_mock.MockerFixture, response: dict):
    """Mocks the ChatGroq model to return a predefined response."""
    mock = mocker.patch("src.adapters.llm.llm.ChatGroq")
    mock.return_value.invoke.return_value = SimpleNamespace(
        content=json.dumps(response)
    )
    return mock


def mock_chatgroq_overview(mocker: pytest_mock.MockerFixture):
    """Mocks the ChatGroq model for game overview responses."""
    return mock_chatgroq(
        mocker,
        {
            "setting": "A mysterious island",
            "beginning": "You wake on a beach",
            "goal": "Escape the island",
        },
    )
