from os import getenv
import pytest
from dotenv import load_dotenv
from starlette.testclient import TestClient
from main import app
load_dotenv()


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello World"}


def test_webhook_get():
    token = getenv("FB_VERIFY_TOKEN")

    response = client.get(
        "/webhook?hub.verify_token="+token+"&hub.mode=subscribe",
        # params={"hub.verify_token": "hub.verify_token", "hub.mode": "subscribe"},
    )
    assert response.status_code == 200
