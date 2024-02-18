from dataclasses import dataclass
import csv

@dataclass
class Customer:

    def __init__(self, id, firstName, lastName, company, address, city, state, zipCode):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.fullAddress = f"{state}" + ", " + f"{city}" + ", " + f"{address}" + ", " + f"{zipCode}"
        self.fullName = f"{firstName}" + " " + f"{lastName}"
        # I'll fix all that fullAddress and fullName stuff once I've figured out how to actually use them

    def custNameAddress(self):
        if self.company == "":
            return f"{self.fullName}\n{self.fullAddress}."
        else:
            return f"{self.fullName}\n{self.fullAddress}\n{self.company}."

    