import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

database = myclient.Client
collection = database.Users
user = {
    'id': '2'
}
result = collection.insert_one(user)
print(result)
user = {
    'id': '3',
    'sex': '4',
    'list': [1,2,3]
}
result = collection.insert_one(user)

