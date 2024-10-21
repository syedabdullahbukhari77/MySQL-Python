import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@AbdullahSyed_aeiou'
)

Local = db.cursor()

def create_database():
    Local.execute("CREATE DATABASE IF NOT EXISTS StudentsDatabase")
    db.commit()
    
create_database()

def using_database():
    Local.execute("USE StudentsDatabase")
    db.commit()
    
using_database()