from flask import Blueprint
from models.User import User
user = Blueprint('user',__name__)

@user.route('/signup',methods=["POST"])
def singup():

    user = User()
    return user.signup()    

# @user.route('/user')
# def getUser():
#     user = User()
#     return user.getUser()