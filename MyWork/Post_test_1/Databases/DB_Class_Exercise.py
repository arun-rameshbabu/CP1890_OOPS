import sqlite3


conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = "CREATE TABLE IF NOT EXISTS movies (id INTEGER AUTO INCREMENT PRIMARY KEY, `name` TEXT, year INTEGER, minutes INTEGER, category TEXT);"
c.execute(query)

# len = 32
c.execute("""insert into movies (name, year, minutes, category)
values ('Spirit: Stallion of the Cimarron', 2002, 83, 'Animation'),
('Spirited Away', 2001, 125, 'Animation'),
('Aladdin', 1992, 90, 'Animation'),
('Ice Age', 2002, 81, 'Animation'),
('Toy Story', 1995, 81, 'Animation'),
('Titanic', 1998, 93, 'History'),
('Transformers', 2005, 100, 'Comedy'),
('Spooky Movie', 1995, 81, 'Comedy'),
('Spookier Movie', 1999, 95, 'Comedy'),
('Spookiest Movie', 2003, 94, 'Comedy'),
('WWII: A History', 2006, 109, 'History'),
('Movie Title', 2007, 100, 'Comedy'),
('Why 13', 2009, 86, 'Comedy');""")
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

    while True:
        com = input("Command: ")
        if com == "cat":
            sort_cat()
        elif com == "year":
            sort_year()
        elif com == "add":
            add_movie()
        elif com == "del":
            del_movie()
        elif com == "exit":
            break
        else:
            print("\nInvalid input, try again")

if __name__ == "__main__":
    main()
