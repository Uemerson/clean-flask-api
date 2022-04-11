from src.data.usecases.add_account.db_add_account import DbAddAccount
from src.data.usecases.add_account.db_add_account_protocols import (
    Encrypter,
    AddAccountModel,
    AccountModel,
    AddAccountRepository,
)
from typing import Tuple
import pytest


def make_encrypter() -> Encrypter:
    class EncrypterStub(Encrypter):
        def encrypt(self, value: str) -> str:
            return "hashed_password"

    return EncrypterStub()


def make_add_account_repository() -> AddAccountRepository:
    class AddAccountRepositoryStub(AddAccountRepository):
        def add(self, account: AddAccountModel) -> AccountModel:
            fake_account = {
                "id": "valid_id",
                "name": "valid_name",
                "email": "valid_email",
                "password": "hashed_password",
            }
            return fake_account

    return AddAccountRepositoryStub()


def make_sut() -> Tuple[DbAddAccount, Encrypter, AddAccountRepository]:
    encrypter_stub = make_encrypter()
    add_account_repository_stub = make_add_account_repository()
    sut = DbAddAccount(encrypter_stub, add_account_repository_stub)
    return sut, encrypter_stub, add_account_repository_stub


def test_should_call_encrypter_with_correct_password(mocker):
    sut, encrypter_stub, _ = make_sut()
    spy = mocker.spy(encrypter_stub, "encrypt")
    account_data = {
        "name": "valid_name",
        "email": "valid_email",
        "password": "valid_password",
    }
    sut.add(account_data)
    spy.assert_called_once_with("valid_password")


def test_should_throw_if_encrypter_throws(mocker):
    with pytest.raises(Exception):
        sut, encrypter_stub, _ = make_sut()
        mocker.patch.object(encrypter_stub, "encrypt", side_effect=Exception())
        account_data = {
            "name": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
        }
        sut.add(account_data)


def test_should_call_add_account_repository_with_correct_values(mocker):
    sut, _, add_account_repository_stub = make_sut()
    spy = mocker.spy(add_account_repository_stub, "add")
    account_data = {
        "name": "valid_name",
        "email": "valid_email",
        "password": "valid_password",
    }
    sut.add(account_data)
    spy.assert_called_once_with(
        {
            "name": "valid_name",
            "email": "valid_email",
            "password": "hashed_password",
        }
    )
