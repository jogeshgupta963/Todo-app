from flask import request,jsonify,make_response
from extensions import mongo
import jwt
# UserCollection = mongo.db.users

class User():
    def signup(self):
        # reading req 
        data = request.get_json()
        # validating data 
        if not data['name'] and not data['email'] and not data['password'] :
            return jsonify({
                "error":"Invalid credentials"
            })
        #finding user
        resp = mongo.db.users.find_one({
            "email":data['email']
        })
        if resp :
            return jsonify({
                "error":"invalid creds"
            })
        # quering mongo 
        resp = mongo.db.users.insert_one(data)
        data['_id'] = str(resp.inserted_id)
        
        # generating jwt
        token = jwt.encode({
             "id":data['_id'],
             "email":data['email']
             },"zxcvbnm","HS256")
        # generating respons
        res = make_response(data)
        # generating cookie
        res.set_cookie("JWT",token)
        return res
    
    def login(self):
        data = request.get_json()

        data = mongo.db.users.find_one({
            "email":data['email']
        })
        #validating user
        if not data:
            return jsonify({
                "error":"Not valid"
            })
        data['_id'] = str(data['_id'])
        #pass match
        if data['password'] != data['password']:
            return jsonify("invalid password")

        #create jwt
        token = jwt.encode({
             "id":data['_id'],
             "email":data['email']
             },"zxcvbnm","HS256")
        res = make_response(data)
        # generating cookie
        res.set_cookie("JWT",token)
        return res

    def getUser(self,currentUser):
        # users = db.users.find()
        resp = mongo.db.users.find()

        users=[]

        for user in resp:
            user["_id"] = str(user['_id'])
            users.append(user)
        # print(type(users))
        # for doc in mongo.db.users.find():
            

        return jsonify(currentUser)