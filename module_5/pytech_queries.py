#Shannon Russell-Phipps
#Module 5.3
#Pytech Queries
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mzkal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.students

docs = students.find({})

print("\nStudents from find query:")
for doc in docs:
    print("Student ID = " + doc["student_id"] + "\nFirst Name = " + doc["first_name"] + "\nLast Name = " + doc["last_name"] + "\n")

print("\nStudents from find one query, each student found separately:")
sam = students.find_one({"student_id": "1007"})
print("Student ID = " + sam["student_id"] +  "\nFirst name = " + sam["first_name"] +  "\nLast name = " + sam["last_name"] + "\n")

scott = students.find_one({"student_id": "1008"})
print("Student ID = " + scott["student_id"] +  "\nFirst name = " + scott["first_name"] +  "\nLast name = " + scott["last_name"]+ "\n")

carol = students.find_one({"student_id": "1009"})
print("Student ID = " + carol["student_id"] +  "\nFirst name = " + carol["first_name"] +  "\nLast name = " + carol["last_name"] + "\n")