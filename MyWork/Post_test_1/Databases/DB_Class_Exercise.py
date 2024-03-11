import sqlite3


conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, `name` TEXT, year INTEGER, minutes INTEGER);"
c.execute(query)
print("Table created successfully")

c.execute("")
conn.commit()
conn.close()


def menu():
    print("\nCOMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")


def categories():
    print("\nCATEGORIES")
    print("1. Animation\n2. Comedy\n3. History")


def main():
    print("The Movie List Program")

    menu()
    categories()

    com = input("Command: ")


if __name__ == "__main__":
    main()