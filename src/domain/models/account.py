from typing import TypedDict


class AccountModel(TypedDict):
    id: str
    name: str
    email: str
    password: str
