import pymongo


class MongoConn:
    client = None
    db = None
    collection = None

    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name

    def connect(self):
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def list_databases(self):
        return self.client.list_database_names()

    def get_collection(self):
        return self.collection.find()

    def get_collection_size(self):
        return self.collection.count_documents({})

    def get_collection_by_name(self, name):
        return self.db[name].find()
