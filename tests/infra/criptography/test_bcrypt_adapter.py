import bcrypt
from src.infra.criptography.bcrypt_adapter import BcryptAdapter


def make_sut():
    salt = bcrypt.gensalt(12)
    return BcryptAdapter(salt), salt


def test_should_call_bcrypt_with_correct_values(mocker):
    sut, salt = make_sut()
    spy = mocker.spy(bcrypt, "hashpw")
    sut.encrypt("any_value")
    spy.assert_called_once_with("any_value".encode(), salt)


def test_should_return_a_hash_os_success(mocker):
    sut, _ = make_sut()
    mocker.patch.object(bcrypt, "hashpw", return_value="hash".encode())
    hash = sut.encrypt("any_value")
    assert hash == "hash"
