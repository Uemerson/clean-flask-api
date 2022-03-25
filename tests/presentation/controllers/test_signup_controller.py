from src.presentation.controllers.signup_controller import SignUpController
from src.presentation.errors.missing_param_error import MissingParamError


def test_should_return_400_if_no_name_is_provided():
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
    assert http_response["body"].args == MissingParamError("name").args


def test_should_return_400_if_no_email_is_provided():
    sut = SignUpController()
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
    sut = SignUpController()
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
    sut = SignUpController()
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