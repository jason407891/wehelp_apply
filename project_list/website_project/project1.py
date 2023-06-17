from flask import request
from flask import redirect
from flask import Flask, render_template
import json
#載入套件
import pymongo
from bson.objectid import ObjectId
#連線到雲端資料庫
client=pymongo.MongoClient("mongodb+srv://root:12root28@cluster0.r39qy0s.mongodb.net/?retryWrites=true&w=majority")


app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static")

app.debug=True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/product")
def product():
    input=request.args.get("item","")
    #進到stock的資料表
    db=client['pteam']
    collection=db['stock']
    results = collection.distinct("Supplier")
    return render_template("product.html",item_output=results)

@app.route("/mfr")
def mfr():
    db=client['pteam']
    collection=db['stock']
    results = collection.distinct("Brand")
    return render_template("mfr.html",item_output=results)

@app.route("/stock")
def stock():
    input=request.args.get("item","")
    db=client['pteam']
    collection=db['stock']
    query={"PartNumber":input}
    results = collection.find(query)
    results=list(results)
    return render_template("stock.html",item_output=results)

@app.route("/upload")
def upload():
    return render_template("upload.html")



app.run(port=3000)