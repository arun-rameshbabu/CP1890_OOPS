import sqlite3

conn = sqlite3.connect('MovieList.sqlite')
c = conn.cursor()
query = ("CREATE TABLE IF NOT EXISTS movies (name TEXT PRIMARY KEY, year INTEGER, minutes INTEGER, categoryID int)")
c.execute(query)
def command_menu():
    print("COMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit Program\n")
    print("CATEGORIES")
    print("1. Animation")
    print("2. Comedy")
    print("3. History\n")

def add():
    name1 = str(input("Name: "))
    year1 = int(input("Year: "))
    minutes1 = int(input("Minutes: "))
    categoryID1 = int(input("CategoryID: "))
    query = ("INSERT INTO movies (name, year, minutes,categoryID) VALUES (?,?,?,?)")
    c.execute(query, (name1, year1, minutes1, categoryID1))
    conn.commit()
    print(f'{name1} was added to database')

def view_by_cat():
    category = int(input("Category: "))
    query = ("SELECT * FROM movies WHERE categoryID = ?")
    c.execute(query, (category,))
    rows = c.fetchall()
    for index,row in enumerate(rows,1):
        print(f"{index}. {row}")

def view_by_year():
    year = int(input("Year: "))
    query = ("SELECT * FROM movies WHERE year = ?")
    c.execute(query, (year,))
    rows = c.fetchall()
    print(f"{'Index':<6}{'Name':<30}{'Year':<10}{'Minutes':<10}{'Category':<10}")
    for index, row in enumerate(rows, 1):
        name, year, minutes, category_id = row
        print(f"{index:<6}{name:<30}{year:<10}{minutes:<10}{category_id:<10}")


def main():
    print("The Movie list program\n")
    command_menu()
    program_running = True
    while program_running == True:
        command = input("Command: ")
        if command == 'add':
            add()
        elif command == 'cat':
            view_by_cat()
        elif command == 'year':
            view_by_year()
        else:
            program_running = False

if __name__ == "__main__":
    main()





