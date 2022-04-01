from src.utils.email_validator import EmailValidatorAdapter


def test_should_return_false_if_validator_returns_false():
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid("invalid_email@mail.com")
    assert is_valid is False
