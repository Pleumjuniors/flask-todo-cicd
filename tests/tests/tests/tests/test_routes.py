def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Todo API' in response.data

def test_health_route(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'

def test_add_todo(client):
    response = client.post('/api/todos', json={'name': 'Write tests'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Write tests'
    assert data['done'] is False

def test_add_todo_existing(client):
    client.post('/api/todos', json={'name': 'Duplicate'})
    response = client.post('/api/todos', json={'name': 'Duplicate'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Duplicate'

def test_get_todo(client):
    response = client.post('/api/todos', json={'name': 'Get me'})
    todo_id = response.get_json()['id']
    response = client.get('/api/todos')
    assert response.status_code == 200
    todos = response.get_json()
    assert any(t['id'] == todo_id and t['name'] == 'Get me' for t in todos)

def test_delete_todo(client):
    response = client.post('/api/todos', json={'name': 'Delete me'})
    todo_id = response.get_json()['id']
    response = client.delete(f'/api/todos/{todo_id}')
    assert response.status_code == 200
    assert response.get_json()['success'] is True

def test_delete_nonexistent_todo(client):
    response = client.delete('/api/todos/9999')
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Todo not found'

def test_todo_missing_name(client):
    response = client.post('/api/todos', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Missing name'

def test_internal_error_handler(client, monkeypatch):
    def broken_query():
        raise Exception("Boom")
    monkeypatch.setattr("app.routes.get_todos", broken_query)
    response = client.get('/api/todos')
    assert response.status_code == 500
    assert response.get_json()['error'] == 'Internal server error'
