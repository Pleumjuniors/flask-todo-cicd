from flask import Blueprint, jsonify, request
from app.models import db, Todo

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@api.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{'id': t.id, 'name': t.name, 'done': t.done} for t in todos])

@api.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    todo = Todo(name=data['name'], done=False)
    db.session.add(todo)
    db.session.commit()
    return jsonify({'id': todo.id, 'name': todo.name, 'done': todo.done}), 201

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'success': True})
