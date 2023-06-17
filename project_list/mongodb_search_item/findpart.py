import pymongo

# 建立与MongoDB的连接
client = pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")
db = client["pteam"]
collection=db['stock']

part_number = ["LM2675M-5.0/NOPB",
                "ADS1220IPWR",
                "ADS1248IPWR",
                "LMZ31710RVQR",
                "LMZ31707RVQR",
                "TPS7B8650QDDARQ1",
                "LM5045SQX/NOPB",
                "TPS16630PWPR",
                "TLV2370IDBVR",
                "LM62460QRPHRQ1",
                "7614-6002PL",
                "AD5308BRUZ-REEL7"
                ]


for part in part_number:
    result = collection.find({"PartNumber": part})

    for item in result:
        print(item)