"""Student, exam and seating arrangement database operations."""
import csv
import math
import os
from pathlib import Path

import mysql.connector as sql


def get_connection():
    return sql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "equiseat"),
    )


def get_sections():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT section FROM student_data WHERE section IS NOT NULL AND section <> '' ORDER BY section")
        return [row[0] for row in cur.fetchall()]
    finally:
        conn.close()


def get_subjects():
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT subid, sub_name, sub_code FROM subjects ORDER BY sub_name")
        return cur.fetchall()
    finally:
        conn.close()


def add_student(name, section, regd_no):
    name, section, regd_no = (name or "").strip(), (section or "").strip(), (regd_no or "").strip()
    if not all((name, section, regd_no)):
        raise ValueError("Student name, section and registration number are required.")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO student_data (regd_no, name, section) VALUES (%s, %s, %s)",
            (regd_no, name, section),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def add_subject(name, code):
    name, code = (name or "").strip(), (code or "").strip().upper()
    if not name or not code:
        raise ValueError("Subject name and subject code are required.")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO subjects (sub_name, sub_code) VALUES (%s, %s)", (name, code))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def add_exam(regd_no, sub_code):
    regd_no, sub_code = (regd_no or "").strip(), (sub_code or "").strip().upper()
    if not regd_no or not sub_code:
        raise ValueError("Registration number and subject code are required.")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO exams (regd_no, sub_code) VALUES (%s, %s)",
            (regd_no, sub_code),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _cell_text(value):
    if value is None:
        return ""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if isinstance(value, float) and math.isnan(value):
            return ""
        if float(value).is_integer():
            return str(int(value))
    return str(value).strip()


def import_students(path):
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream))
    elif suffix in (".xlsx", ".xls"):
        try:
            import pandas as pd
        except ImportError as exc:
            raise RuntimeError("Excel import requires pandas and openpyxl. Install requirements.txt.") from exc
        rows = pd.read_excel(path).to_dict(orient="records")
    else:
        raise ValueError("Only .csv, .xlsx and .xls files are supported.")
    if not rows:
        raise ValueError("The import file contains no student rows.")
    conn = get_connection()
    inserted = 0
    try:
        cur = conn.cursor()
        for row in rows:
            normalized = {str(key).strip().lower(): value for key, value in row.items()}
            regd = _cell_text(normalized.get("regd_no", normalized.get("rollno", "")))
            name = _cell_text(normalized.get("name", ""))
            section = _cell_text(normalized.get("section", ""))
            if not all((regd, name, section)):
                raise ValueError("Each row must contain regd_no, name and section columns.")
            cur.execute(
                "INSERT INTO student_data (regd_no, name, section) VALUES (%s, %s, %s)",
                (regd, name, section),
            )
            inserted += 1
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return inserted


def get_data(sections):
    if not sections:
        return {}
    placeholders = ", ".join(["%s"] * len(sections))
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            f"""SELECT e.regd_no, e.sub_code
                FROM exams e
                INNER JOIN student_data s ON s.regd_no = e.regd_no
                WHERE s.section IN ({placeholders})
                ORDER BY e.regd_no, e.sub_code""",
            tuple(sections),
        )
        student_subjects = {}
        for regd_no, sub_code in cur.fetchall():
            student_subjects.setdefault(regd_no, set()).add(sub_code)
        return student_subjects
    finally:
        conn.close()


def get_rooms(rooms_list):
    if not rooms_list:
        return []
    placeholders = ", ".join(["%s"] * len(rooms_list))
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            f"SELECT room_name, num_rows, num_cols FROM rooms WHERE room_name IN ({placeholders}) ORDER BY room_name",
            tuple(rooms_list),
        )
        return cur.fetchall()
    finally:
        conn.close()


def arrange(student_subject_dict, room_list):
    if not student_subject_dict:
        return []
    room_specs = get_rooms(room_list)
    if not room_specs:
        raise ValueError("Select at least one valid room.")
    students = sorted(student_subject_dict)
    capacity = sum(rows * cols for _, rows, cols in room_specs)
    if len(students) > capacity:
        raise ValueError(f"{len(students)} students selected, but selected rooms hold only {capacity}.")
    assignments = []
    for room_name, rows, cols in room_specs:
        grid = [[None for _ in range(cols)] for _ in range(rows)]
        assignments.append((room_name, grid))
    student_index = 0
    for _, grid in assignments:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if student_index >= len(students):
                    break
                candidate_index = next(
                    (index for index in range(student_index, len(students))
                     if _placement_valid(grid, row, col, students[index], student_subject_dict)),
                    student_index,
                )
                students[student_index], students[candidate_index] = (
                    students[candidate_index], students[student_index]
                )
                grid[row][col] = students[student_index]
                student_index += 1
    return assignments


def _placement_valid(grid, row, col, student, subject_map):
    subjects = subject_map.get(student, set())
    for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] is not None:
            if subjects.intersection(subject_map.get(grid[r][c], set())):
                return False
    return True
