from flask import Flask, render_template, request, jsonify,url_for
import pdf_gen
import arrange_algo as arr
import addrooms_be as room
app=Flask(__name__)
app.template_folder = "templates"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/arrange", methods=["POST"])
def arrange():
    selected_rooms = request.form.getlist('room')
    selected_sections = request.form.getlist('section')
    matrices = arr.arrange(arr.get_data(selected_sections), selected_rooms)
    pdf_gen.generate_pdfs_for_matrices(matrices)
    return 'generated succesfully!!'

@app.route("/arrangepage")
def arrangestuds():
    return render_template("seating.html")

@app.route("/addroom", methods=["POST"])
def add_room():
    room_name = request.form['roomname']
    rows = request.form['rows']
    cols = request.form['cols']
    room.add_rooms(room_name, rows, cols)
    return 'Room added successfully!'

@app.route('/deleteroom', methods=["POST"])
def delete_room():
    room_name = request.form['roomname']
    room.delete_room(room_name)
    return 'Room deleted successfully!'

@app.route("/roomspage")
def addrooms():
    return render_template("addrooms.html")    

@app.route("/subspage")
def addsubs():
    return render_template("sub.html")

@app.route("/studentspage")
def addstudents():
    return render_template("adstudents.html")

@app.route("/addstudent", methods=["POST"])
def add_student():
    student_name = request.form['studentname']
    section = request.form['section']
    roll_no = request.form['rollno']
    add_student(student_name, section, roll_no)
    return 'Student added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
