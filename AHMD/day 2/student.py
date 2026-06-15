import json
student=[
    {
        "id": 100,
        "name": "AHMD",
        "mark": 90
    },
    {
        "id": 101,
        "name": "ABERR",
        "mark": 88
    },
    {
        "id": 102,
        "name": "FADHII",
        "mark": 75
    },
    {
        "id": 103,
        "name": "DEEVV",
        "mark": 65
    },
    {
        "id": 104,
        "name": "SHYAAM",
        "mark": 55
    }
]
with open("students.json","w")as f:
    json.dump(student,f,indent=2)
with open("students.json", "r") as f:
    print(f.read())
with open("students.json", "r") as f:
    data = json.load(f)
for student in data:
    print(
        f"ID: {student['id']}, "
        f"Name: {student['name']}, "
        f"Mark: {student['mark']}"
    )