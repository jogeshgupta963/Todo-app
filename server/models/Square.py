from flask import jsonify,request
from flask_restful import Resource

class Square(Resource):
    
    def get(self,num):
        return jsonify(num*num)