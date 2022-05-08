from operator import truth
from src.infra.db.mongodb.helpers.mongo_helper import MongoHelper
from src.infra.db.mongodb.account_repository.account import AccountMongoRepository
from pymongo import MongoClient
import mongomock


def make_mongo_helper() -> MongoHelper:
    class MongoHelperStub(MongoHelper):
        __client: MongoClient = mongomock.MongoClient()

        def get_collection(self, name: str):
            return self.__client.db[name]
    return MongoHelperStub()


def make_sut() -> AccountMongoRepository:
    mongo_helper_stub = make_mongo_helper()
    sut = AccountMongoRepository(mongo_helper_stub)
    return sut


def test_should_return_an_account_on_success():
    sut = make_sut()
    account = sut.add(
        {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
        }
    )
    assert truth(account) is True
    assert truth(account['id']) is True
    assert account['name'] == 'any_name'
    assert account['email'] == 'any_email@mail.com'
    assert account['password'] == 'any_password'
