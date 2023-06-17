import pymongo

# 建立与MongoDB的连接
client = pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")

# 选择数据库
db = client["pteam"]
collection=db['supplier']
data={"supplier_name":"oneyac","brand":["TDK","YAGEO","KEMET","TE","KYOCERA","NEXPERIA","CHILISIN","KYOCERA AVX","PANJIT"]}
result=collection.insert_one(data)