from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
ma = Marshmallow()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shinde.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(400), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name

# Create TodoList Schema
class TodolistSchema(ma.Schema):
    class Meta:
        fields = ("name", 'description', 'completed', 'date_created')

todolist_schema = TodolistSchema(many=False)
todolists_schema = TodolistSchema(many=True)

@app.route("/add_todo", methods=["POST"])
def add_todo():
    with app.app_context():
        try:
            name = request.json["name"]
            description = request.json["description"]
            completed = request.json["completed"]

            new_todo = Todolist(name=name, description=description, completed = completed)
            db.session.add(new_todo)
            db.session.commit()

            return todolist_schema.dump(new_todo)
        except Exception as e:
            return jsonify({"Error": "Invalid Request"})

@app.route("/get_todo", methods=["GET"])
def get_todos():
    todos = Todolist.query.all()
    result = todolists_schema.dump(todos)
    return jsonify(result)

@app.route("/get_todo/<int:id>", methods=["GET"])
def get_todo(id):
    todo = Todolist.query.get_or_404(int(id))
    result = todolist_schema.dump(todo)
    return jsonify(result)

@app.route("/update/<int:id>", methods = ["PUT"])
def update_todo(id):
    todo = Todolist.query.get_or_404(int(id))

    name = request.json["name"]
    description = request.json["description"]
    completed = request.json["completed"]

    todo.name = name
    todo.description = description
    todo.completed = completed

    db.session.commit()

    return todolist_schema.jsonify(todo)

@app.route("/delete_todo/<int:id>", methods=["DELETE"])
def del_todo(id):
    todo = Todolist.query.get_or_404(int(id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"success":"Todo deleted"})

@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"Error": "404 Not Found"})

if __name__ == "__main__":
    app.run(debug=True)
