from src.data.usecases.add_account.db_add_account import DbAddAccount
from src.data.protocols.encrypter import Encrypter
from typing import Tuple
import pytest


def make_encrypter() -> Encrypter:
    class EncrypterStub(Encrypter):
        def encrypt(self, value: str) -> str:
            return "hashed_password"

    return EncrypterStub()


def make_sut() -> Tuple[DbAddAccount, Encrypter]:
    encrypter_stub = make_encrypter()
    sut = DbAddAccount(encrypter_stub)
    return sut, encrypter_stub


def test_should_call_encrypter_with_correct_password(mocker):
    sut, encrypter_stub = make_sut()
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
        sut, encrypter_stub = make_sut()
        mocker.patch.object(encrypter_stub, "encrypt", side_effect=Exception())
        account_data = {
            "name": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
        }
        sut.add(account_data)
