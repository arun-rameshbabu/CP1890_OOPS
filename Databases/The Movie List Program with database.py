import sqlite3 as sql
from dataclasses import dataclass
DATASOURCE ='Movies.sqlite'

@dataclass
class Movie:
    ID:int
    Name:str
    Year:int
    Mins:int
    Category:str

def create_database():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    m.execute("""CREATE TABLE IF NOT EXISTS Movies (ID integer primary key, Name varchar(30),Year integer , Mins integer , Category varchar(20));""")
    movies.close()

def read_db():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()

    m.execute("""SELECT * FROM Movies""")

    moviesList = m.fetchall()

    movies.close()
    return moviesList

def insert_db(Movie):
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    query = f"""INSERT INTO Movies ({Movie.ID},{Movie.Name},{Movie.Year},{Movie.Mins},{Movie.Category}) VALUES ('{Movie}"""
    m.execute(query)
    movies.commit()
    movies.close()
def readCategories():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    query = f"""SELECT Category FROM Movies"""
    m.execute(query)
    categories = m.fetchall()
    movies.close()

    return categories
def showCategories():
    categories = readCategories()

    print('CATEGORIES')
    categoriesList = tuple(set(categories))
    for i, category in enumerate(categoriesList,start=1):
        print(f'{i}. {category}')

def cat():
    categories = readCategories()

    categoriesList = tuple((set(categories)))
    i = int(input('Category ID: '))
    category = categoriesList[i-1]

    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    query = f"""SELECT * FROM Movies WHERE Category = {category}"""
    m.execute(query)
    M_C = m.fetchall()
    movies.close()


    print()
    print('MOVIES - {}'.format(category.upper()))
    print('{:<4} {:25} {:<4} {:<4} {:15}'.format('ID', 'Name', 'Year', 'Mins', 'Category'))
    print('-'*70)
    for movie in M_C:
        print('{:<4} {:25} {:<4} {:<4} {:15}'.format(movie[0], movie[1], movie[2], movie[3],movie[4]))



def add ():
    movies = read_db()
    i = len(movies)

    categories = readCategories()
    categoriesList = tuple(set(categories))

    movie = Movie(i,input('Name: '), int(input('Year: ')), int(input('Minutes: ')), categoriesList[int(input('Category:')) - 1] )