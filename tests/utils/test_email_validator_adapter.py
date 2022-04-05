from src.utils.email_validator import EmailValidatorAdapter
import validators


def test_should_return_false_if_validator_returns_false(mocker):
    mocker.patch.object(validators, "email", return_value=False)
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid("invalid_email@mail.com")
    assert is_valid is False


def test_should_return_true_if_validator_returns_true():
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid("valid_email@mail.com")
    assert is_valid is True
