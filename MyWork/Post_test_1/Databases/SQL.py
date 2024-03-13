"""
ACID
Atomicity, Consistency, Isolation, Durability

"""
from dataclasses import dataclass


@dataclass
class Movie:
    sr_number: int
    genre: str
    name: str
    year: int
    actors: str


"""
sr_num | genre | name | year | actors
-------------------------------------
       |       |      |      |          
-------|-------|------|------|          
       |       |      |      |          

"""

"""
sqlite3

conn = connect("path_to_database")

c = conn.cursor()


"""