from src.presentation.errors.missing_param_error import MissingParamError
from src.presentation.helpers.http_helper import bad_request


class SignUpController:
    def handle(self, http_request):
        required_fields = ["name", "email", "password"]
        for field in required_fields:
            if http_request["body"].get(field) == None:
                return bad_request(MissingParamError(field))
