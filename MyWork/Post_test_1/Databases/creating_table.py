import sqlite3

# if db doesn't exist, it creates one
conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, `Name` TEXT, age INTEGER, marks INTEGER);"
c.execute(query)
print("Table created successfully")

c.execute("insert into students values (1, 'Arun Rameshbabu', 30, 100);")
conn.commit()
conn.close()


