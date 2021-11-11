from json import dumps
from werkzeug.security import check_password_hash

from utils.mongo import db_config
from model.users import Users

def user_log(cons,name,password):
        db_config()
        param : str = cons
        if cons=="email":
            logged_user = Users.objects.get(email=name)

        else:
            logged_user = Users.objects.get(username=name)


        if name ==logged_user[param] and check_password_hash(
            logged_user["password"],password
        ):
            message = "user logged in successfully."
            return message
        
        else:
            message = "Invalid username or password"
            return message