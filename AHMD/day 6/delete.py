import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
name = "deevv"
cursor.execute(
    "DELETE FROM students WHERE name = ?",
    (name,)
)
conn.commit()
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print("\nRemaining Students:")
for student in students:
    print(
        f"ID: {student[0]}, "
        f"Name: {student[1]}, "
        f"Marks: {student[2]}"
    )
conn.close()