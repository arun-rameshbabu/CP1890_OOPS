#importing the module
import sqlite3

#connecting to a database file
conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = "SELECT * FROM Product"
c.execute(query)
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)

#---------------------------------------------------------------------

conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = "SELECT productName FROM Product WHERE listPrice > 450"
c.execute(query)
rows = c.fetchall()
conn.close()

print()
for row in rows:
    print(row)

#---------------------------------------------------------------------

conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = "select categoryName, productName, listprice from Product join Category	where Product.categoryID = Category.categoryID order by listprice asc"
c.execute(query)
rows = c.fetchall()
conn.close()

print("\nPRODUCTS:")
print(f"{'Category':<12}{'Name':<30}{'Price':<10}")
print("==================================================")
for row in rows:
    if len(row[1]) > 30:
        shr = row[1][:25] + '...'
        print(f"{row[0]:<12}{shr:<30}{row[2]:<10}")
    else:
        print(f"{row[0]:<12}{row[1]:<30}{row[2]:<10}")