import sqlite3
from movie_list_classes import Category, Movie

# conn = sqlite3.connect('movies.sqlite')
# c = conn.cursor()
# create_query = ("create table if not exists movies ("
#          "id integer primary key autoincrement, "
#          "Name text not null, "
#          "Year int not null, "
#          "Mins int not null, "
#          "Category text not null)")
# c.execute(create_query)
#
# categories = ('Animation', 'Comedy', 'History')
conn = None


def connect_to_db(conn):
    db_file = "movies.sqlite"
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row


def close_db(conn):
    if conn:
        conn.close()


def make_category(row):
    return Category(row['categoryID'], row['categoryName'])


def make_movie(row):
    return Movie(row['movieID'], row['name'], row['year'], row['minutes'], make_category(row))


def get_categories(conn):
    query = '''SELECT categoryID, categoryName FROM Category'''
    cursor = conn.cursor()
    cursor.excute(query)
    results = cursor.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories


def get_category(conn, category_id):
    query = '''SELECT categoryID, name as categoryName FROM Category WHERE categoryID = ?'''
    cursor = conn.cursor()
    cursor.excute(query, (category_id,))
    row = cursor.fetchone()
    if row:
        return make_category(row)
    else:
        return None


def make_movie_list(list_movies):
    movies = []
    for row in list_movies:
        movies.append(make_movie(row))
    return movies


def get_movies_by_category(conn, category_id):
    query = '''SELECT movieID, Movie.name, year, minutes, Movie.categoryID, Category.name as categoryName 
    FROM Movie JOIN Category ON Movie.categoryID = Category.categoryID WHERE Movie.categoryID = ?'''
    cursor = conn.cursor()
    cursor.excute(query, (category_id,))
    results = cursor.fetchall()

    return make_movie_list(results)


def add_movie(conn, movie):
    query = '''INSERT INTO Movie (categoryId, name, year, minutes) VALUES (?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.excute(query, (movie.category.id, movie.name, movie.year, movie.minutes))
    conn.commit()


def ui():
    print("The Movie List Program\n")

    print("COMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")


def display_categories():
    print("CATEGORIES")


def cat_command():
    query = ("select * from movies "
             "order by category")
    c.execute(query)


def year_command():
    query = ("select * from movies "
             "order by year desc")
    c.execute(query)


# def add_command():
#     name = input("Name: ")
#     year = input("Year: ")
#     category = input("Category: ")
#
#     query = ("insert into movies values ("
#              "default, "
#              "n, "
#              "year, "
#              "Category)")
#
#     c.excute(query)


def main():
    ui()

    while True:
        command = input("\nCommand: ")
        if command == 'cat':
            cat_command()
        elif command == 'year':
            year_command()
        elif command == 'add':
            add_command()
        elif command == 'del':
            del_command()
        elif command == 'exit':
            print('\nBye!')
            break


if __name__ == "__main__":
    main()
