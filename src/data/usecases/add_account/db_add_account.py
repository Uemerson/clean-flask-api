from src.domain.usecases.add_account import AddAccount, AddAccountModel
from src.domain.models.account import AccountModel
from src.data.protocols.encrypter import Encrypter


class DbAddAccount(AddAccount):
    def __init__(self, encrypter: Encrypter):
        self._encrypter = encrypter

    def add(self, account: AddAccountModel) -> AccountModel:
        self._encrypter.encrypt(account["password"])
        return None
