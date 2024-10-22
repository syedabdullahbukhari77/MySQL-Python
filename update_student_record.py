import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='studentsdatabase'
)

Local = db.cursor()

def Update_Table():
    sql_UpdateNames = """
                    UPDATE students
                    SET first_name = 'Hasan Shah', last_name ='Askari', age = 20 
                    WHERE first_name = 'Ahmad' AND last_name = 'Abdullah' AND age = 30;           
                """
    Local.execute(sql_UpdateNames)
    db.commit()

Update_Table()
