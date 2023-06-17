import pandas as pd
from pymongo import MongoClient

# 连接 MongoDB
client = MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")
db = client['pteam']
collection = db['stock']

# 从 MongoDB 中读取数据
data = list(collection.find())

# 创建 DataFrame 对象
df = pd.DataFrame(data)

# 导出为 Excel 文件
df.to_excel(r"D:\User\Downloads\stockdata0605123.xlsx", index=False)