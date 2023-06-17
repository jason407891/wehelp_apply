import pymongo

# 建立與 MongoDB 的連接
client = pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")
db = client["pteam"]
collection = db["stock"]

string=20230607
# 設定查詢的變數
query = {"date":string}

# 使用變數進行查詢
result = collection.delete_many(query)
