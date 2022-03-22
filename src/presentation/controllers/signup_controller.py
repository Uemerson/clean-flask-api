from src.presentation.errors.missing_param_error import MissingParamError
from src.presentation.helpers.http_helper import bad_request


class SignUpController:
    def handle(self, http_request):
        if "name" not in http_request["body"]:
            return bad_request(MissingParamError("name"))
        if "email" not in http_request["body"]:
            return bad_request(MissingParamError("email"))
