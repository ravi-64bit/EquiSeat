"""EquiSeat: simple exam seating arrangement web app."""
import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

import arrange_algo as arr
import addrooms_be as rooms_db
import pdf_gen

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-only-change-me")
app.config["GENERATED_FOLDER"] = str(Path(app.root_path) / "generated")
app.config["UPLOAD_FOLDER"] = str(Path(app.root_path) / "uploads")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
Path(app.config["GENERATED_FOLDER"]).mkdir(exist_ok=True)
Path(app.config["UPLOAD_FOLDER"]).mkdir(exist_ok=True)


@app.route("/")
def index():
    try:
        room_list = rooms_db.list_rooms()
        sections = arr.get_sections()
        return render_template("index.html", rooms=room_list, sections=sections)
    except Exception as exc:
        app.logger.exception("Unable to load dashboard")
        flash(f"Database is not ready: {exc}", "error")
        return render_template("index.html", rooms=[], sections=[])


@app.route("/roomspage")
def room_page():
    return render_template("addrooms.html", rooms=rooms_db.list_rooms())


@app.route("/addroom", methods=["POST"])
def add_room():
    try:
        rooms_db.add_room(
            request.form.get("roomname", ""),
            request.form.get("rows", ""),
            request.form.get("cols", ""),
        )
        flash("Room added successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")
    except Exception as exc:
        app.logger.exception("Unable to add room")
        flash(f"Could not add room: {exc}", "error")
    return redirect(url_for("room_page"))


@app.route("/deleteroom", methods=["POST"])
def delete_room():
    try:
        rooms_db.delete_room(request.form.get("roomname", ""))
        flash("Room deleted successfully.", "success")
    except Exception as exc:
        app.logger.exception("Unable to delete room")
        flash(f"Could not delete room: {exc}", "error")
    return redirect(url_for("room_page"))


@app.route("/studentspage")
def students_page():
    return render_template("adstudents.html", sections=arr.get_sections())


@app.route("/addstudent", methods=["POST"])
def add_student():
    try:
        arr.add_student(
            request.form.get("studentname", ""),
            request.form.get("section", ""),
            request.form.get("rollno", ""),
        )
        flash("Student added successfully.", "success")
    except Exception as exc:
        app.logger.exception("Unable to add student")
        flash(f"Could not add student: {exc}", "error")
    return redirect(url_for("students_page"))


@app.route("/uploadstudents", methods=["POST"])
def upload_students():
    upload = request.files.get("student_file")
    if not upload or not upload.filename:
        flash("Choose a CSV or Excel file first.", "error")
        return redirect(url_for("students_page"))
    filename = secure_filename(upload.filename)
    if not filename:
        flash("The uploaded filename is invalid.", "error")
        return redirect(url_for("students_page"))
    path = Path(app.config["UPLOAD_FOLDER"]) / filename
    upload.save(path)
    try:
        count = arr.import_students(path)
        flash(f"Imported {count} student record(s).", "success")
    except Exception as exc:
        app.logger.exception("Student import failed")
        flash(f"Import failed: {exc}", "error")
    finally:
        path.unlink(missing_ok=True)
    return redirect(url_for("students_page"))


@app.route("/subspage")
def subjects_page():
    return render_template("sub.html", subjects=arr.get_subjects())


@app.route("/addsubject", methods=["POST"])
def add_subject():
    try:
        arr.add_subject(request.form.get("subname", ""), request.form.get("subcode", ""))
        flash("Subject added successfully.", "success")
    except Exception as exc:
        app.logger.exception("Unable to add subject")
        flash(f"Could not add subject: {exc}", "error")
    return redirect(url_for("subjects_page"))


@app.route("/addexam", methods=["POST"])
def add_exam():
    try:
        arr.add_exam(request.form.get("rollno", ""), request.form.get("subcode", ""))
        flash("Exam registered successfully.", "success")
    except Exception as exc:
        app.logger.exception("Unable to register exam")
        flash(f"Could not register exam: {exc}", "error")
    return redirect(url_for("subjects_page"))


@app.route("/arrangepage")
def arrange_page():
    return render_template(
        "seating.html",
        rooms=rooms_db.list_rooms(),
        sections=arr.get_sections(),
    )


@app.route("/arrange", methods=["POST"])
def arrange():
    selected_rooms = request.form.getlist("room")
    selected_sections = request.form.getlist("section")
    try:
        if not selected_rooms or not selected_sections:
            raise ValueError("Select at least one room and one section.")
        matrices = arr.arrange(arr.get_data(selected_sections), selected_rooms)
        if not matrices:
            flash("No registered exam candidates were found for those sections.", "error")
            return redirect(url_for("arrange_page"))
        generated = pdf_gen.generate_pdfs_for_matrices(
            matrices, selected_rooms, app.config["GENERATED_FOLDER"]
        )
        flash(f"Generated {len(generated)} seating PDF(s).", "success")
        return render_template("seating.html", rooms=rooms_db.list_rooms(),
                               sections=arr.get_sections(), generated=generated)
    except Exception as exc:
        app.logger.exception("Seating arrangement failed")
        flash(f"Could not generate seating: {exc}", "error")
        return redirect(url_for("arrange_page"))


@app.route("/generated/<path:filename>")
def generated_file(filename):
    return send_from_directory(app.config["GENERATED_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
