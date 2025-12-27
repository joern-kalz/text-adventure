"""Tests for the POST /perform-action endpoint."""

import pytest_mock
from fastapi.testclient import TestClient
from src.adapters.api.app import create_app
from tests.mock_chatgroq import mock_chatgroq, mock_chatgroq_overview


def test_perform_action_success(mocker: pytest_mock.MockerFixture):
    """Tests performing an action successfully."""
    client = TestClient(create_app())
    mock_chatgroq_overview(mocker)
    start_response = client.post("/start-game").json()
    fixture = {
        "outcome": "You swing and hit!",
        "quests": ["Find the key"],
        "inventory": ["rusty sword"],
        "world": "The door is open",
    }
    mock_chatgroq(mocker, fixture)

    resp = client.post(
        "/perform-action",
        json={"action": "look around"},
        headers={"x-session-token": start_response["session_token"]},
    )

    assert resp.status_code == 200
    assert resp.json() == fixture


def test_perform_action_with_invalid_session():
    """Tests performing an action with an invalid session."""
    client = TestClient(create_app())

    resp = client.post(
        "/perform-action",
        json={"action": "look around"},
        headers={"x-session-token": "invalid_session_id"},
    )

    assert resp.status_code == 404


def test_perform_action_history_persistence(mocker: pytest_mock.MockerFixture):
    """Tests that chat history is persisted across actions."""
    client = TestClient(create_app())
    mock_chatgroq_overview(mocker)
    start_response = client.post("/start-game").json()
    fixture = {
        "outcome": "Outcome",
        "quests": [],
        "inventory": [],
        "world": "World",
    }
    mock_chatgroq(mocker, fixture)

    client.post(
        "/perform-action",
        json={"action": "first action"},
        headers={"x-session-token": start_response["session_token"]},
    )

    mock = mock_chatgroq(mocker, fixture)
    client.post(
        "/perform-action",
        json={"action": "second action"},
        headers={"x-session-token": start_response["session_token"]},
    )

    args, _ = mock.return_value.invoke.call_args
    assert "first action" in str(args[0])
    assert "second action" in str(args[0])
