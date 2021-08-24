import pytest
from starlette.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello World"}


def test_webhook_get():
    response = client.get(
        "/webhook",
        params={"hub.verify_token": "hub.verify_token", "hub.mode": "subscribe"},
    )
    assert response.status_code == 200
