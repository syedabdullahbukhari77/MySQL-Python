import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@AbdullahSyed_aeiou',
    database='studentsdatabase'
)

Local = db.cursor()

def create_table ():
    
    sql_Creatingtable = '''
                CREATE TABLE students (first_name VARCHAR(50), last_name VARCHAR(50), age smallint UNSIGNED)
                '''
    Local.execute(sql_Creatingtable)
    db.commit()
    for table in Local:
        print(table)
create_table()