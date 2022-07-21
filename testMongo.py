import pymongo

client = pymongo.MongoClient("mongodb+srv://anujy17:mongo123@cluster0.hvhyqko.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)
d={"name":"anuj","age":25,"surname":"yadav"}
db1=client["mongotest"]
coll=db1['test']
coll.insert_one(d)