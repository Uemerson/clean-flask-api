from pymongo import MongoClient


class MongoHelper:
    __client: MongoClient

    def connect(self, uri: str) -> None:
        self.__client = MongoClient(uri)

    def disconnect(self) -> None:
        self.__client.close()

    def get_collection(self, name: str):
        return self.__client.db[name]
