import datetime
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, DictField, EmailField, StringField


class Users(Document):
    name = StringField(required=True)
    gender = StringField(choices=("male","female","other"))
    phone_number = StringField()
    address = DictField()
    username = StringField(required=True, unique=True,min_length=3,max_length=16)
    email = EmailField(required=True,unique=True)
    password = StringField(required=True,min_length=8)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
