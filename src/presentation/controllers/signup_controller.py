from src.presentation.errors.missing_param_error import MissingParamError


class SignUpController:
    def handle(self, http_request):
        if "name" not in http_request["body"]:
            return {"statusCode": 400, "body": MissingParamError("name")}
        if "email" not in http_request["body"]:
            return {
                "statusCode": 400,
                "body": MissingParamError("email"),
            }
