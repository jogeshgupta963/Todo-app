from flask import jsonify,make_response,request
from extensions import mongo
import bson
class Todo():
    def createTodo(current_user):
        data = request.get_json()
        data['user'] = bson.ObjectId(oid=current_user['_id'])
        res = mongo.db.todos.insert_one(data)

        data['_id'] = str(res.inserted_id)
        data['user'] = str(data['user'])
        resp = make_response(data)
        return resp
    def getAllTodos(current_user):
       
        resp = mongo.db.todos.find({'user':bson.ObjectId(oid=current_user['_id'])})
        todos=[]
        for todo in resp :
            todo["_id"] = str(todo["_id"])
            todo["user"] = str(todo["user"])
            todos.append(todo)
        return make_response(todos)

    def deleteTodo(todo):

        resp = mongo.db.todos.find_one_and_delete({
            "_id":bson.ObjectId(oid=todo)
        })
        resp["_id"] = str(resp["_id"])
        resp["user"] = str(resp["user"])
        return make_response(resp)

