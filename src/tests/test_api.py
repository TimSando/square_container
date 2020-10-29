from pathlib import Path

import requests

import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


@pytest.mark.parametrize("expected", [(200)])
def test_heartbeat(expected):
    response = client.get("/utils/heartbeat")
    assert response.status_code == expected
    assert response.text == "{}"
