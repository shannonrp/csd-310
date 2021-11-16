#Shannon Russell-Phipps
#Module 6.3
#Pytech delete
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mzkal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.students
#Find
docs = students.find({})

print("\nStudents from find query:")
for doc in docs:
    print("Student ID = " + doc["student_id"] + "\nFirst Name = " + doc["first_name"] + "\nLast Name = " + doc["last_name"] + "\n")

#Student info
bucky = {
    "student_id": "1010",
    "first_name": "Bucky",
    "last_name": "Barnes",
    "enrollment": [
        {
            "term": "Fall 2021",
            "gpa": "3.0",
             "start_date": "10/18/2021",
             "end_date": "12/19/2021",
            "course": [
                {
                    "course_id": "com200",
                    "description": "Communications",
                    "instructor": "Clint Barton",
                    "grade": "B",
                },
                {
                    "course_id": "mar200",
                    "description": "Marketing",
                    "instructor": "Natasha Romanov",
                    "grade": "B",
                }
            ]
        }
    ]
}
#Insert
bucky_student_id = students.insert_one(bucky).inserted_id
print("Inserted student Bucky Barnes into the students collection, " + str(bucky_student_id))
#Print inserted student
bucky = students.find_one({"student_id": "1010"})
print("Student ID = " + bucky["student_id"] +  "\nFirst name = " + bucky["first_name"] +  "\nLast name = " + bucky["last_name"] + "\n")
#Delete new student
bucky_student_id = students.delete_one(bucky)
#Find students
docs = students.find({})

print("\nStudents from find query:")
for doc in docs:
    print("Student ID = " + doc["student_id"] + "\nFirst Name = " + doc["first_name"] + "\nLast Name = " + doc["last_name"] + "\n")

input("\n\n End of program, press any key to exit...")