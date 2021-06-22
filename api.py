from flask import Flask , request
import pymongo
import json
from bson.json_util import dumps


app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb+srv://s1j2v326ari:s1j2v326ari@projects.luhuo.mongodb.net/drinks?retryWrites=true&w=majority")
mydb = myclient['drinks']
mycol = mydb["drinksCol"]

#function which returns all of the drinks in the db
@app.route('/api/drinks',methods = ["GET"])
def drinks():
    result = mycol.find()
    result = dumps(list(result))
    return result

#function which returns a drink from the db by receiving a data by the user
@app.route('/api/drinks/<brand>')
def get_drink_by_Brand(brand):
    query = mycol.find({"brand":brand})
    result = dumps(list(query))
    return result

#function that receives a drink from user and adds it to the db
@app.route("/api/addDrink", methods = ["POST"])
def add_drink():
    brand = request.json["brand"]
    price = request.json["price"]
    name = request.json["name"]
    mycol.insert_one({"brand":brand, "price":price, "name":name})
    return "201"

#function that receives a db.drink from user and updates it
@app.route("/api/updateDrink/<drinks_name>",methods = ["PUT"])
def update_drink(drinks_name):
    brand = request.json["brand"]
    price = request.json["price"]
    name = request.json["name"]
    old_drink = {"name": drinks_name}
    new_drink = {"$set": {"brand":brand, "price":price, "name":name}}
    mycol.update_one(old_drink,new_drink)
    return "201"

@app.route("/api/deleteDrink/<drinks_name>",methods = ["DELETE"])
def delete_drink(drinks_name):
    drink = {"name":drinks_name}
    mycol.delete_one(drink)
    return "200"

#function that sorts the drinks by price (low - high)
@app.route("/api/drinks/sortPrice")
def sort_price():
    result = mycol.find().sort("price",1)
    result = dumps(list(result))
    return result


# myclient.close() - need to check
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
