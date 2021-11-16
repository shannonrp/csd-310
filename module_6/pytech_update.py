#Shannon Russell-Phipps
#Module 6.2
#Pytech update

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mzkal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.students
#Find all
docs = students.find({})

print("\nStudents from find query:")
for doc in docs:
    print("Student ID = " + doc["student_id"] + "\nFirst Name = " + doc["first_name"] + "\nLast Name = " + doc["last_name"] + "\n")
#Update one
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Barnes"}})
#Print updated student info
print("\nStudents from find one query:")
sam = students.find_one({"student_id": "1007"})
print("Student ID = " + sam["student_id"] +  "\nFirst name = " + sam["first_name"] +  "\nLast name = " + sam["last_name"] + "\n")

input("\n\n End of program, press any key to exit...")

