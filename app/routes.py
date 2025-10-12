from flask import jsonify
from app.models import Todo, db

def register_routes(app):
    @app.route("/")
    def home():
        return "สวัสดีจาก Flask!"

    @app.route("/todos")
    def get_todos():
        todos = Todo.query.all()
        if not todos:
            return jsonify({"message": "ยังไม่มีข้อมูล TODO"})
        return jsonify([{"id": t.id, "task": t.task, "done": t.done} for t in todos])
