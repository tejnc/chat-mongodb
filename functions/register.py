from json import loads,dumps
from werkzeug.security import generate_password_hash

from utils.mongo import db_config
from model.users import Users


def register(event,context):
    """
        registering or signing up user
    """
    body = loads(event["body"])
    _name = body["name"]
    _gender = body["gender"]
    _phone_number = body["phone_number"]
    _province = body["province"]
    _district = body["district"]
    _town = body["town"]
    _username = body["username"]
    _email = body["email"]
    _password = body["password"]

    _hashed_password = generate_password_hash(_password)

    db_config()

    new_user = Users(
        name = _name,
        gender = _gender,
        phone_number = _phone_number,
        address = {
            "province":_province,
            "district":_district,
            "town":_town
        },
        username = _username,
        email = _email,
        password = _hashed_password
    )
    new_user.save()

    return dumps({"message":"user saved"})