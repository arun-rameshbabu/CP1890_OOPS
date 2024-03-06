"""
Assignment 2

Classes
"""

from dataclasses import dataclass

# Question 1:
@dataclass
class Person:
    fname: str
    lname: str
    email: str
    
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"


@dataclass
class Customer(Person):
    number: str


@dataclass
class Employee(Person):
    ssn: str
