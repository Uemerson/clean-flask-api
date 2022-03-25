from src.presentation.controllers.signup_controller import SignUpController
from src.presentation.errors.missing_param_error import MissingParamError
from src.presentation.errors.invalid_param_error import InvalidParamError


def make_sut():
    class EmailValidatorStub:
        def is_valid(self, email):
            return True

    email_validator_stub = EmailValidatorStub()
    sut = SignUpController(email_validator_stub)
    return sut, email_validator_stub


def test_should_return_400_if_no_name_is_provided():
    sut, _ = make_sut()
    http_request = {
        "body": {
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == MissingParamError("name").args


def test_should_return_400_if_no_email_is_provided():
    sut, _ = make_sut()
    http_request = {
        "body": {
            "name": "any_name",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == MissingParamError("email").args


def test_should_return_400_if_no_password_is_provided():
    sut, _ = make_sut()
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == MissingParamError("password").args


def test_should_return_400_if_no_password_confirmation_is_provided():
    sut, _ = make_sut()
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == MissingParamError("password_confirmation").args


def test_should_return_400_if_an_invalid_email_is_provided(mocker):
    sut, email_validator_stub = make_sut()
    mocker.patch.object(email_validator_stub, "is_valid", return_value=False)
    http_request = {
        "body": {
            "name": "any_name",
            "email": "invalid_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == InvalidParamError("email").args
