import os
from dotenv import load_dotenv
import requests
from utils.config import BASE_URL

load_dotenv()
TOKEN = os.getenv("GOREST_TOKEN")
assert TOKEN is not None

def test_get_users():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{BASE_URL}/users", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user_success():
    payload = {
        "name": "Test User",
        "email": "testuser12345@example.com",
        "gender": "male",
        "status": "active"
    }
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
