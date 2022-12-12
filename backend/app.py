from flask import Flask
from todo.todo import todo
from user.user import user
from extensions import mongo
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://172.17.0.3:27017/myDatabase"
mongo.init_app(app)

app.register_blueprint(user)
app.register_blueprint(todo)


if __name__ == "__main__":
    app.run(debug=True)