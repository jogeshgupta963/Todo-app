from flask import request,jsonify
# from flask_pymongo import PyMongo
# from ..extensions import mongo
from app import db

# UserCollection = mongo.db.users


class User():
    def signup(self):
        data = request.get_json()
        return jsonify(data)
    
    def getUser(self):
        # users = db.users.find()
        users = db.users.find()
        return jsonify(users)