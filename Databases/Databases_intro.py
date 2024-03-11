import sqlite3

conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()

query = ("SELECT ProductName FROM product where categoryID = 1  ")
c.execute(query)
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)