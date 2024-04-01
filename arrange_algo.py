import mysql.connector as sql

def get_data(sections):
    conn = sql.connect(
        host='localhost',
        user='root',
        password='',
        database='equiseat'
    )
    cursor = conn.cursor()
    query = "SELECT regd_no, sub_code FROM exams" 
    cursor.execute(query)
    res = cursor.fetchall()
    student_sub_dict = {}
    for row in res:
        stu_id, sub_id = row
        student_sub_dict.setdefault(stu_id, []).append(sub_id)
    return student_sub_dict


def get_rooms(rooms_list):
    conn = sql.connect(
        host='localhost',
        user='root',
        password='',
        database='equiseat'
    )
    cursor = conn.cursor()
    query = "SELECT num_rows, num_cols FROM rooms WHERE room_name IN ('{}')".format(','.join(rooms_list))
    cursor.execute(query)
    res = cursor.fetchall()
    size_list = [(rows, cols) for rows, cols in res]
    cursor.close()
    conn.close() 
    return size_list
    

 
def get_room_matrix(room_sizes):
  room_matix = []
  for room in room_sizes:
    size1, size2 = room
    zero_matrix = [[0] * size2 for _ in range(size1)]
    room_matix.append(zero_matrix)
  return room_matix

def trans(matrix):
    transpose=[]
    for list in matrix:
        temp=list
        for  i in range(len(list)):
            for j in range (len(matrix[0])):
                temp[j][i]=list[i][j]
        transpose.append(temp)
    return transpose


def arrange(student_subject_dict,room_list):
    subs = set()
    for value_list in student_subject_dict.values():
        for element in value_list:
            subs.add(element)
    
    if len(subs) == 0:
        return 0
    elif len(subs) == 1:
        return arrange_sequential(student_subject_dict,room_list)
    else:
        return arrange_studs(student_subject_dict,get_room_matrix(get_rooms(room_list)))

    
def arrange_sequential(dict, room_list):
    students = list(dict.keys())
    all_rooms = get_room_matrix(get_rooms(room_list))
    stud_index = 0
    for room in all_rooms:
        for row in range(len(room)):
            for col in range(len(room[row])):
                room[row][col] = students[stud_index]
                stud_index = (stud_index + 1) % len(students)
    return trans(all_rooms)


            
def arrange_studs(student_subject_dict,matrix):
    arranged_matrix = matrix
    students = list(student_subject_dict.keys())
    
    def is_valid_placement(row, col, student):
        neighbors = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        ]
        for r, c in neighbors:
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and arranged_matrix[r][c] == student_subject_dict[student]:
                return False
        return True
    
    student_index = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0 and student_index < len(students):
                while student_index < len(students):
                    student = students[student_index]
                    if is_valid_placement(row, col, student):
                        arranged_matrix[row][col] = student
                        student_index += 1
                        break
                    student_index += 1
            elif student_index >= len(students):
                break
    return trans(arranged_matrix)


