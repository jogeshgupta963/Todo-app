from flask import jsonify,request
from flask_restful import Resource
class Hello(Resource):
    
    def get(self):
        return jsonify("Get on /")
    
    def post(self):
        data = request.get_json()
        print(data)
        return jsonify(data)
