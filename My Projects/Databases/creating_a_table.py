import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = ("create table if not exists students ("
         "id integer primary key, "
         "First_Name text, "
         "Last_Name text, "
         "age integer, "
         "marks integer)")
c.execute(query)
print("Table has been created")

c.execute("insert into students values("
          "1, "
          "'Tyson', "
          "'Harris', "
          "19, "
          "100)")
conn.commit()

conn.close()
