from .db_add_account_protocols import AddAccount, AddAccountModel, AccountModel, Encrypter, AddAccountRepository


class DbAddAccount(AddAccount):
    def __init__(self, encrypter: Encrypter, add_account_repository: AddAccountRepository):
        self._encrypter = encrypter
        self._add_account_repository = add_account_repository

    def add(self, account: AddAccountModel) -> AccountModel:
        hashed_password = self._encrypter.encrypt(account["password"])
        account_data = dict(account, **{"password": hashed_password})
        self._add_account_repository.add(account_data)
        return None
