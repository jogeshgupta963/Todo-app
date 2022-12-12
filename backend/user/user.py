from flask import Blueprint
# from .models.User import User
from user.User import User
from middleware.middleware import token_required
user = Blueprint('user',__name__)


@user.route('/signup',methods=["POST"])
def singup():

    user = User()
    return user.signup()    


@user.route('/login',methods=["POST"])
def login():
    user = User()
    return user.login()

@user.route('/user')
@token_required
def getUser(current_user):
    user = User()
    return user.getUser(current_user)