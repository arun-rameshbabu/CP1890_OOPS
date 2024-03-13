import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()

query = """CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks INTEGER)"""

c.execute(query)
print("Table created successfully")

query = ("""Insert into students values ({}{}{}{})""" format (3,'Harv', 18, 100)
c.execute(query)
conn.commit()
conn.close()


