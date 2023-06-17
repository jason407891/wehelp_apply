import pymongo

# 建立與 MongoDB 的連接
client = pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")
db = client["pteam"]
collection = db["stock"]

part="ERG-3SJ820"
# 設定查詢的變數
query = {"PartNumber":part}

# 使用變數進行查詢
result = collection.find(query)

# 輸出查詢結果
for document in result:
    print(document)