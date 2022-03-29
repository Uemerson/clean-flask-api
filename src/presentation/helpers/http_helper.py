from src.presentation.protocols.http import HttpResponse
from src.presentation.errors.server_error import ServerError


def bad_request(error: Exception) -> HttpResponse:
    return {"statusCode": 400, "body": error}


def server_error() -> HttpResponse:
    return {"statusCode": 500, "body": ServerError()}
