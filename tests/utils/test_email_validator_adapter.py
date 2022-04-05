from src.utils.email_validator_adapter import EmailValidatorAdapter
import validators


def make_sut() -> EmailValidatorAdapter:
    return EmailValidatorAdapter()


def test_should_return_false_if_validator_returns_false(mocker):
    mocker.patch.object(validators, "email", return_value=False)
    sut = make_sut()
    is_valid = sut.is_valid("invalid_email@mail.com")
    assert is_valid is False


def test_should_return_true_if_validator_returns_true():
    sut = make_sut()
    is_valid = sut.is_valid("valid_email@mail.com")
    assert is_valid is True


def test_call_validator_with_correct_email(mocker):
    sut = make_sut()
    spy = mocker.spy(validators, "email")
    sut.is_valid("any_email@mail.com")
    spy.assert_called_once_with("any_email@mail.com")
