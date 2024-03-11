import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()

query = ("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks INTEGER)")

c.execute(query)
print("Table created successfully")

c.execute("Insert into students (name, age, marks) values (1,2,3)")


