from src.presentation.controllers.signup_controller import SignUpController


def test_return_400_if_no_name_is_provided():
    sut = SignUpController()

    http_request = {
        "body": {
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }

    http_response = sut.handle(http_request)

    assert http_response["statusCode"] == 400
    assert http_response["body"].args == Exception("Missing param: name").args

    print("should return 400 if no name is provided")
