from .db_add_account_protocols import AddAccount, AddAccountModel, AccountModel, Encrypter, AddAccountRepository


class DbAddAccount(AddAccount):
    def __init__(self, encrypter: Encrypter, add_account_repository: AddAccountRepository):
        self._encrypter = encrypter
        self._add_account_repository = add_account_repository

    def add(self, account_data: AddAccountModel) -> AccountModel:
        hashed_password = self._encrypter.encrypt(account_data["password"])
        account = self._add_account_repository.add(dict(account_data, **{"password": hashed_password}))
        return account
