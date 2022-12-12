from flask import Blueprint
from todo.Todo import Todo
from middleware.middleware import token_required
todo = Blueprint("todo",__name__)

@todo.route('/todos',methods=["POST"])
@token_required
def createTodo(current_user):
    return Todo.createTodo(current_user)


@todo.route('/todos',methods=["GET"])
@token_required
def getAllTodos(current_user):
    return Todo.getAllTodos(current_user)

@todo.route('/todos/<string:todo>',methods=["DELETE"])
@token_required
def deletetodos(current_user,todo):
    return Todo.deleteTodo(todo)