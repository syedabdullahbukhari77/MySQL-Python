import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@AbdullahSyed_aeiou',
    database='StudentsDatabase'
)

Local = db.cursor()

def show_tableContent():
    sql_command = 'ALTER TABLE students RENAME'
    
    Local.execute(sql_command)

    for All_tables in Local:
        print(All_tables)
        
    
show_tableContent()