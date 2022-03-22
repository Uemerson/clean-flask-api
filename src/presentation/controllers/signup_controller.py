class SignUpController:
    def handle(self, http_request):
        if "name" not in http_request["body"]:
            return {"statusCode": 400, "body": Exception("Missing param: name")}
        if "email" not in http_request["body"]:
            return {"statusCode": 400, "body": Exception("Missing param: email")}
