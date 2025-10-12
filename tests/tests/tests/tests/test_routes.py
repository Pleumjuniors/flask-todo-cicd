def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"สวัสดีจาก Flask!" in response.data

def test_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert b"ยังไม่มีข้อมูล TODO" in response.data
