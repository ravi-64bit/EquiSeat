"""Database helpers for exam rooms."""
import os
import mysql.connector as sql


def get_connection():
    return sql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "equiseat"),
    )


def list_rooms():
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT rid, room_name, num_rows, num_cols FROM rooms ORDER BY room_name")
        return cur.fetchall()
    finally:
        conn.close()


def add_room(name, rows, cols):
    name = (name or "").strip()
    try:
        rows, cols = int(rows), int(cols)
    except (TypeError, ValueError):
        raise ValueError("Rows and columns must be whole numbers.")
    if not name or len(name) > 5:
        raise ValueError("Room name is required and must be at most 5 characters.")
    if rows < 1 or cols < 1 or rows > 100 or cols > 30:
        raise ValueError("Room dimensions must be between 1–100 rows and 1–30 columns.")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO rooms (room_name, num_rows, num_cols) VALUES (%s, %s, %s)",
            (name, rows, cols),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def delete_room(name):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM rooms WHERE room_name = %s", ((name or "").strip(),))
        if cur.rowcount == 0:
            raise ValueError("Room not found.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# Backwards-compatible names used in the original project.
add_rooms = add_room
remove_room = delete_room
