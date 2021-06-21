import  pymongo

myclient = pymongo.MongoClient("mongodb+srv://s1j2v326ari:s1j2v326ari@projects.luhuo.mongodb.net/drinks?retryWrites=true&w=majority")

mydb = myclient['drinks']
mycol = mydb["drinksCol"]

drinks = [{"brand": "coca cola", "name":"sprite", "price":12}
        ,{"brand": "flavoured water", "name":"grape fruit", "price":20},
        {"brand": "coca cola", "name":"coke", "price":5}]

x = mycol.insert_many(drinks)
print(x.inserted_ids)
