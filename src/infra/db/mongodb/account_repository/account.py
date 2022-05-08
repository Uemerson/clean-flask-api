from src.infra.db.mongodb.helpers.mongo_helper import MongoHelper
from src.data.protocols.add_account_repository import AddAccountRepository
from src.domain.usecases.add_account import AddAccountModel
from src.domain.models.account import AccountModel


class AccountMongoRepository(AddAccountRepository):
    __mongo_helper: MongoHelper

    def __init__(self, mongo_helper: MongoHelper) -> None:
        self.__mongo_helper = mongo_helper

    def add(self, account_data: AddAccountModel) -> AccountModel:
        account_collection = self.__mongo_helper.get_collection('accounts')
        account = account_collection.insert_one({**account_data})
        return {**account_data, 'id': str(account.inserted_id)}
