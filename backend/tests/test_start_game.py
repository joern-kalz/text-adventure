"""Tests for the POST /start-game endpoint."""

import pytest_mock
from dirty_equals import IsStr
from fastapi.testclient import TestClient
from src.adapters.api.app import create_app
from tests.mock_chatgroq import mock_chatgroq


def test_start_game_returns_overview(mocker: pytest_mock.MockerFixture):
    client = TestClient(create_app())
    fixture = {
        "setting": "A mysterious island",
        "beginning": "You wake on a beach",
        "goal": "Escape the island",
    }
    mock_chatgroq(mocker, fixture)

    response = client.post("/start-game")

    assert response.status_code == 200
    assert response.json() == fixture | {"token": IsStr()}
