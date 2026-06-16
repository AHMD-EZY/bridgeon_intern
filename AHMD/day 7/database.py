import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def create_task(title: str):
    conn = get_connection()

    cursor = conn.execute(
        "INSERT INTO tasks(title, completed) VALUES(?, ?)",
        (title, 0)
    )

    conn.commit()

    task_id = cursor.lastrowid

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return dict(task)


def get_tasks(status=None):
    conn = get_connection()

    if status == "pending":
        rows = conn.execute(
            "SELECT * FROM tasks WHERE completed = 0"
        ).fetchall()

    elif status == "completed":
        rows = conn.execute(
            "SELECT * FROM tasks WHERE completed = 1"
        ).fetchall()

    else:
        rows = conn.execute(
            "SELECT * FROM tasks"
        ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def update_task(task_id, title=None, completed=None):
    conn = get_connection()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    ).fetchone()

    if not task:
        conn.close()
        return None

    title = title if title is not None else task["title"]
    completed = completed if completed is not None else task["completed"]

    conn.execute(
        """
        UPDATE tasks
        SET title=?, completed=?
        WHERE id=?
        """,
        (title, int(completed), task_id)
    )

    conn.commit()

    updated = conn.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    ).fetchone()

    conn.close()

    return dict(updated)


def delete_task(task_id):
    conn = get_connection()

    cursor = conn.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()

    deleted = cursor.rowcount > 0

    conn.close()

    return deleted