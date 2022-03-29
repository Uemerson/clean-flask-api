from src.presentation.errors import InvalidParamError, MissingParamError
from src.presentation.helpers.http_helper import bad_request, server_error
from src.presentation.protocols.http import HttpResponse, HttpRequest
from presentation.protocols.controller import Controller


class SignUpController(Controller):
    def __init__(self, email_validator):
        self._email_validator = email_validator

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            required_fields = ["name", "email", "password", "password_confirmation"]
            for field in required_fields:
                if http_request["body"].get(field) is None:
                    return bad_request(MissingParamError(field))
            if http_request["body"]["password"] != http_request["body"]["password_confirmation"]:
                return bad_request(InvalidParamError("password_confirmation"))
            is_valid = self._email_validator.is_valid(http_request["body"]["email"])
            if not is_valid:
                return bad_request(InvalidParamError("email"))
        except Exception:
            return server_error()
