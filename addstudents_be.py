import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='equiseat'
)
cursor = conn.cursor()


excel_data = pd.read_excel('Book1.xlsx')

for index, row in excel_data.iterrows():
    query = "INSERT INTO students(regd_no,name,section) VALUES (%s, %s, %s)"
    values = (row['regd_no'], row['name'], row['section']) 
    cursor.execute(query, values)

conn.commit()
cursor.close()
conn.close()
