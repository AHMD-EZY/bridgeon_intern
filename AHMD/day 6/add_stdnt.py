import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for Student {i + 1}")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
conn.commit()
print("\nStudents inserted successfully!")
conn.close()