from app.main import app

def test_welcome():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Welcome mani"