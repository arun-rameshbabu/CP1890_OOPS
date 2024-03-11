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
