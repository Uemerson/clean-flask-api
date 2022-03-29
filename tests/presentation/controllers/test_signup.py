from src.presentation.controllers.signup import SignUpController
from src.presentation.protocols import EmailValidator
from src.presentation.errors import InvalidParamError, MissingParamError, ServerError
from src.domain.models.account import AccountModel
from src.domain.usecases.add_account import AddAccount, AddAccountModel
from typing import Tuple


def make_email_validator() -> EmailValidator:
    class EmailValidatorStub(EmailValidator):
        def is_valid(self, email: str) -> bool:
            return True

    return EmailValidatorStub()


def make_add_account() -> AddAccount:
    class AddAccountStub(AddAccount):
        def add(self, account: AddAccountModel) -> AccountModel:
            fake_account = {
                "id": "valid_id",
                "name": "valid_name",
                "email": "valid_email@mail.com",
                "password": "valid_password",
            }
            return fake_account

    return AddAccountStub()


def make_sut() -> Tuple[SignUpController, EmailValidator, AddAccount]:
    email_validator_stub = make_email_validator()
    add_account_stub = make_add_account()
    sut = SignUpController(email_validator_stub, add_account_stub)
    return sut, email_validator_stub, add_account_stub


def test_should_return_400_if_no_name_is_provided():
    sut, *_ = make_sut()
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
    sut, *_ = make_sut()
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
    sut, *_ = make_sut()
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
    sut, *_ = make_sut()
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


def test_should_return_400_if_password_confirmation_fails():
    sut, *_ = make_sut()
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "invalid_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 400
    assert http_response["body"].args == InvalidParamError("password_confirmation").args


def test_should_return_400_if_an_invalid_email_is_provided(mocker):
    sut, email_validator_stub, *_ = make_sut()
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


def test_should_call_email_validator_with_correct_email(mocker):
    sut, email_validator_stub, *_ = make_sut()
    spy = mocker.spy(email_validator_stub, "is_valid")
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    sut.handle(http_request)
    spy.assert_called_once_with("any_email@mail.com")


def test_should_return_500_if_email_validator_throws(mocker):
    sut, email_validator_stub, *_ = make_sut()
    mocker.patch.object(email_validator_stub, "is_valid", side_effect=Exception())
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 500
    assert http_response["body"].args == ServerError().args


def test_should_call_add_account_with_correct_values(mocker):
    sut, _, add_account_stub = make_sut()
    spy = mocker.spy(add_account_stub, "add")
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    sut.handle(http_request)
    spy.assert_called_once_with(
        {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
        }
    )


def test_should_return_500_if_add_account_throws(mocker):
    sut, _, add_account_stub = make_sut()
    mocker.patch.object(add_account_stub, "add", side_effect=Exception())
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "password_confirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["statusCode"] == 500
    assert http_response["body"].args == ServerError().args
