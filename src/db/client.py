from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

db_client = MongoClient(MONGO_URI)

db = db_client['keewproyect']

class ClientDB:

    def insert_one(self, collection_name, data):
        collection = db[collection_name]
        collection.insert_one(data)


    def find_one(self, collection_name, filter = {}):
        collection = db[collection_name]
        hola = collection.find_one(filter, {'_id': 0})
        return collection.find_one(filter, {'_id': 0, 'password' : 0})
    
    def find_one_for_login(self, collection_name, filter = {}):
        collection = db[collection_name]
        return collection.find_one(filter, {'_id': 0})
        
    def test_mongo(self, collection_name,):
        collection = db[collection_name]
        print(collection)
        print("perros")
        return {"hopla" : collection.name,
                "db": db.name}