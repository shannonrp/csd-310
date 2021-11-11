#Shannon Russell-Phipps
#Assignment 5.2
#11/10/2021
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mzkal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("\n--Pytech Collection--")
print(db.list_collection_names())
input("\n\n End of program, press any key to exit...")