import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='StudentsDatabase'
)

Local = db.cursor()

def show_table ():
    sql_command = '''DELETE FROM `students` 
                     WHERE `first_name` is NULL AND `last_name` is NULL AND `age` is NULL AND 
                     `Email`='syedabdullahbukhari77@gmail.com';
                     '''
    Local.execute(sql_command)
    db.commit()
    
    Local.execute("SELECT * FROM students")
    for table in Local:
        print(table)
show_table()
