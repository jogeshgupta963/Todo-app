from flask import Flask
from routes.user import user
from routes.user import user
import pymongo
app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

app.register_blueprint(user)
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

if __name__ == "__main__":
    app.run(debug=True)