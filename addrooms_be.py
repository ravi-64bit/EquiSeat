import mysql.connector as sql


def conn():
    mydb = sql.connect(
        host="localhost",
        user="root",
        password="",
        database="equiseat"
    )
    cursor = mydb.cursor()
    return cursor

def add_rooms(name,r,c):
    rows=int(r)
    cols=int(c)
    cursor=conn()
    query="INSERT INTO rooms(room_name,num_rows,num_cols) VALUES('{}','{}','{}')".format(name,r,c)
    cursor.execute(query)
    msg='Room added successfully!'

def remove_room(name):
    cursor=sql.connect(
        host='localhost',
        user='root',
        password='',
        database='equiseat'
    )
    query="DELETE FROM rooms WHERE name='{}'".format(name)
    cursor.execute(query)
    msg2="Deleted Successfully"
