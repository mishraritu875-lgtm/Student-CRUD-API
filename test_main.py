from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_create_student():
    student = {
        "name": "Amit",
        "date_of_birth": "2003-05-15",
        "email": "amit.test@example.com",
        "phone": "9876543210"
    }

    response = client.post("/students", json=student)

    assert response.status_code == 201
    assert response.json()["name"] == "Amit"


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200


def test_invalid_email():
    student = {
        "name": "Rahul",
        "date_of_birth": "2003-05-15",
        "email": "invalid-email",
        "phone": "9876543210"
    }

    response = client.post("/students", json=student)
    assert response.status_code == 422