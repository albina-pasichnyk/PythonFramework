from pymongo import MongoClient


class BaseMongo:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def find(self, query):
        return list(self.collection.find(query))

    def find_one(self, query):
        return self.collection.find_one(query)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def update_one(self, query, key_to_update):
        return self.collection.update_one(query, key_to_update)

    def update_many(self, query, key_to_update):
        return self.collection.update_many(query, key_to_update)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def delete_many(self, query):
        return self.collection.delete_many(query)

    def sorting(self, key, sorting_type: str):
        if sorting_type == 'asc':
            return self.collection.find().sort(key, 1)
        elif sorting_type == 'desc':
            return self.collection.find().sort(key, -1)
