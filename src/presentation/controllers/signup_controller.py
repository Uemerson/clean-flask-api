class SignUpController:
    def handle(self, http_request):
        return {"statusCode": 400, "body": Exception("Missing param: name")}
