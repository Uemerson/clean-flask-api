from typing import Any
from src.presentation.protocols import HttpResponse
from src.presentation.errors.server_error import ServerError


def bad_request(error: Exception) -> HttpResponse:
    return {"statusCode": 400, "body": error}


def server_error() -> HttpResponse:
    return {"statusCode": 500, "body": ServerError()}


def ok(data: Any) -> HttpResponse:
    return {"statusCode": 200, "body": data}
