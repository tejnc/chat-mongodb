from mongoengine import connect


from utils.constants import MONGO_PASS, MONGO_DB


def get_db_connection():
    url = "mongodb+srv://test:{}@cluster0.x25kn.mongodb.net/{}?retryWrites=true&w=majority".format(
        MONGO_PASS, MONGO_DB
    )
    return url


def db_config():
    try:
        uri: str = get_db_connection()
        connect(host=uri)
    except KeyError:
        connect("mongoenginetest", host="mongomock://localhost")
