from app.models import Todo, db

def test_create_todo(app):
    with app.app_context():
        todo = Todo(task="เขียนโค้ด", done=False)
        db.session.add(todo)
        db.session.commit()
        assert todo.id == 1
