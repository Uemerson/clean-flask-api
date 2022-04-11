from src.domain.usecases.add_account import AddAccountModel
from src.domain.models.account import AccountModel


class AddAccountRepository:
    def add(self, account: AddAccountModel) -> AccountModel:
        pass
