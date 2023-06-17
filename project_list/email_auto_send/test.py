import customer_list
import pandas as pd

# 讀取Excel檔案
df = pd.read_excel('emailbot.xlsx')

# 將Excel數據轉換為字典
data_dict = df.to_dict()

# 打印字典

#print(data_dict)

for key, value in data_dict.items():
    print(key, value)

"""
for i in range(0,10):
    print(data_dict['email'][i], end=" ")
    print(data_dict['name'][i])
"""



"""
for data in customer_list.list():
    print(data["name"])
    print(data["email"])
"""