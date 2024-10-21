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

def SelectingAllFromThetables():
    sql_CommandFor_FirstName =  """
                                SELECT first_name FROM students
                                """
    Local.execute(sql_CommandFor_FirstName)

    # Create an empty list to store the results
    first_names = []

    # Iterate through the results and append each first name to the list
    for table in Local:
        first_names.append(table[0])  # Access the first element of the tuple (first_name)

    # Print the list of first names
    print(f'Here is the information about you : {first_names[0]}')
    
    db.commit()

SelectingAllFromThetables()
