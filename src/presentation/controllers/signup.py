from src.domain.usecases.add_account import AddAccount
from src.presentation.errors import InvalidParamError, MissingParamError
from src.presentation.helpers.http_helper import bad_request, server_error, ok
from src.presentation.protocols import HttpResponse, HttpRequest, Controller, EmailValidator


class SignUpController(Controller):
    def __init__(self, email_validator: EmailValidator, add_account: AddAccount):
        self._email_validator = email_validator
        self._add_account = add_account

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
            account = self._add_account.add(
                {
                    "name": http_request["body"]["name"],
                    "email": http_request["body"]["email"],
                    "password": http_request["body"]["password"],
                }
            )
            return ok(account)
        except Exception:
            return server_error()
