from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api
from models.Hello import Hello
from models.Square import Square
app = Flask(__name__)
api=Api(app)

api.add_resource(Hello,'/')
api.add_resource(Square,'/square/<int:num>')

if __name__ == "__main__":
    app.run(debug=True)