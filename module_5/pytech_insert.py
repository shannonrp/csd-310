#Shannon Russell-Phipps
#Module 5.3
#Pytech insert
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mzkal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Student info
sam = {
    "student_id": "1007",
    "first_name": "Sam",
    "last_name": "Wilson",
    "enrollment": [
        {
            "term": "Fall 2021",
            "gpa": "4.0",
             "start_date": "10/18/2021",
             "end_date": "12/19/2021",
            "course": [
                {
                    "course_id": "com200",
                    "description": "Communications",
                    "instructor": "Clint Barton",
                    "grade": "A",
                },
                {
                    "course_id": "mar200",
                    "description": "Marketing",
                    "instructor": "Natasha Romanov",
                    "grade": "A",
                }
            ]
        }
    ]
}
scott = {
    "student_id": "1008",
    "first_name": "Scott",
    "last_name": "Lang",
    "enrollment": [
        {
            "term": "Fall 2021",
            "gpa": "2.5",
             "start_date": "10/18/2021",
             "end_date": "12/19/2021",
            "course": [
                {
                    "course_id": "com200",
                    "description": "Communications",
                    "instructor": "Clint Barton",
                    "grade": "C",
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
carol = {
    "student_id": "1009",
    "first_name": "Carol",
    "last_name": "Danvers",
    "enrollment": [
        {
            "term": "Fall 2021",
            "gpa": "4.0",
             "start_date": "10/18/2021",
             "end_date": "12/19/2021",
            "course": [
                {
                    "course_id": "com200",
                    "description": "Communications",
                    "instructor": "Clint Barton",
                    "grade": "A",
                },
                {
                    "course_id": "mar200",
                    "description": "Marketing",
                    "instructor": "Natasha Romanov",
                    "grade": "A",
                }
            ]
        }
    ]
}

students = db.students

sam_student_id = students.insert_one(sam).inserted_id
print("Inserted student Sam Wilson into the students collection, " + str(sam_student_id))

scott_student_id = students.insert_one(scott).inserted_id
print("Inserted student Scott Lang into the students collection, " + str(scott_student_id))

carol_student_id = students.insert_one(carol).inserted_id
print("Inserted student Carol Danvers into the students collection, " + str(carol_student_id))