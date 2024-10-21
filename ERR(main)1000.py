import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@AbdullahSyed_aeiou',
    database='StudentsDatabase'
)

Local = db.cursor()

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

# Create a Person object
person = Person("John Doe", 30, "johndoe@example.com")

# Prepare the SQL statement
sql = "INSERT INTO persons (name, age, email) VALUES (%s, %s, %s)"

# Convert person object to a tuple
values = (person.name, person.age, person.email)

# Execute the statement
Local.execute(sql, values)

db.commit()

print("Data inserted successfully")