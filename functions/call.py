from json import dumps


def call(events, context):
    return dumps({"message": "working"})
