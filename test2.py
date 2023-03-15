from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
print("Connection Successful")
db = client["example"]
col = db["temp"]
x = col.find()
for i in x:
    print(i)

