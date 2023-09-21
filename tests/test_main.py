from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello DataScience Applications!"}


def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == [{"ProductName": "A"}, {"ProductName": "B"}]
