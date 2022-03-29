from typing import TypedDict
from src.domain.models.account import AccountModel


class AddAccountModel(TypedDict):
    name: str
    email: str
    password: str


class AddAccount:
    def add(self, account: AddAccountModel) -> AccountModel:
        pass
