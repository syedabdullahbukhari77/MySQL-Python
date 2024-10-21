import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@AbdullahSyed_aeiou'
)

Local = db.cursor()

def using_database():
    Local.execute("USE StudentsDatabase")
    db.commit()
    
using_database()

def inserting_values_intoTable():
    sql_valuesInTable = """INSERT INTO students 
                           VALUES ('Ahmad', 'Abdullah' , 30)""" 
    
    Local.execute(sql_valuesInTable)
    db.commit()
    
inserting_values_intoTable()

def Show_table ():
    Local.execute('SELECT * FROM Students')
    
    for table in Local:
        print(table)
Show_table()