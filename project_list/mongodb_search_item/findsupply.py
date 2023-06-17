import pymongo

# 建立与MongoDB的连接
client = pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")
db = client["pteam"]
collection=db['stock']

supply=collection.distinct('Supplier')
print(supply)