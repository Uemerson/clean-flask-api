import bcrypt
from src.infra.criptography.bcrypt_adapter import BcryptAdapter


def test_should_call_bcrypt_with_correct_values(mocker):
    salt = bcrypt.gensalt(12)
    sut = BcryptAdapter(salt)
    spy = mocker.spy(bcrypt, "hashpw")
    sut.encrypt("any_value")
    spy.assert_called_once_with("any_value".encode(), salt)
