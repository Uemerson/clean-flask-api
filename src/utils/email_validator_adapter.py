from src.presentation.protocols.email_validator import EmailValidator
import validators


class EmailValidatorAdapter(EmailValidator):
    def is_valid(self, email: str) -> bool:
        return False if not validators.email(email) else True
