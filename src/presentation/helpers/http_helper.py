from src.presentation.errors.server_error import ServerError


def bad_request(error):
    return {"statusCode": 400, "body": error}


def server_error():
    return {"statusCode": 500, "body": ServerError()}
