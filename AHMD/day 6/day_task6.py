import sqlite3

def get_connection():
    return sqlite3.connect("students.db")


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    print("Table created successfully.")


def insert_student(name, marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )

    conn.commit()
    conn.close()

    print("Student inserted successfully.")


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if students:
        print("\n=== All Students ===")
        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("No students found.")

    conn.close()


def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Marks: {student[2]}"
        )
    else:
        print("Student not found.")

    conn.close()


def update_marks(student_id, new_marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Marks updated successfully.")
    else:
        print("Student not found.")

    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    conn.close()


def get_students_above(threshold):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )

    students = cursor.fetchall()

    if students:
        print(f"\n=== Students with marks above {threshold} ===")

        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("No matching students found.")

    conn.close()


def main():
    create_table()

    while True:
        print("\n===== STUDENT DATABASE SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student By ID")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Students Above Marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            insert_student(name, marks)

        elif choice == "2":
            get_all_students()

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            get_student_by_id(student_id)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            new_marks = int(input("Enter new marks: "))
            update_marks(student_id, new_marks)

        elif choice == "5":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == "6":
            threshold = int(input("Enter threshold marks: "))
            get_students_above(threshold)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()