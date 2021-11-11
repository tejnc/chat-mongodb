from json import loads, dumps

from functions.extra import user_log

def login(event,context):
    body = loads(event["body"])
    _keys = body.keys()

    if "username" in _keys:
        _username = body["username"]
        _password = body["password"]

        cons = "username"
        msg = user_log(cons,_username,_password)
        return dumps({"message":msg})

    elif "email" in _keys:
        _email = body["email"]
        _password = body["password"]
        cons = "email"

        msg = user_log(cons,_email,_password)
        return dumps({"message":msg})

    else:
        return dumps({"message":"error"})

    

        
        
