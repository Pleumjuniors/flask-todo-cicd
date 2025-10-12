from app.models import Todo

def test_todo_model():
    todo = Todo(name='Test Task', done=False)
    assert todo.name == 'Test Task'
    assert todo.done is False
