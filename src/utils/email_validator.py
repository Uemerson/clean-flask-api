from src.presentation.protocols.email_validator import EmailValidator
import validators


class EmailValidatorAdapter(EmailValidator):
    def is_valid(self, email: str) -> bool:
        try:
            return validators.email(email)
        except validators.ValidationFailure:
            return False
