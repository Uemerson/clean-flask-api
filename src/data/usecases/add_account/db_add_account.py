from .db_add_account_protocols import AddAccount, AddAccountModel, AccountModel, Encrypter


class DbAddAccount(AddAccount):
    def __init__(self, encrypter: Encrypter):
        self._encrypter = encrypter

    def add(self, account: AddAccountModel) -> AccountModel:
        self._encrypter.encrypt(account["password"])
        return None
