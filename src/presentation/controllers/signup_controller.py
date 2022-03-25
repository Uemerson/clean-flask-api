from src.presentation.errors.missing_param_error import MissingParamError
from src.presentation.errors.invalid_param_error import InvalidParamError
from src.presentation.errors.server_error import ServerError
from src.presentation.helpers.http_helper import bad_request


class SignUpController:
    def __init__(self, email_validator):
        self._email_validator = email_validator

    def handle(self, http_request):
        try:
            required_fields = ["name", "email", "password", "password_confirmation"]
            for field in required_fields:
                if http_request["body"].get(field) == None:
                    return bad_request(MissingParamError(field))
            is_valid = self._email_validator.is_valid(http_request["body"]["email"])
            if not is_valid:
                return bad_request(InvalidParamError("email"))
        except:
            return {"statusCode": 500, "body": ServerError()}
