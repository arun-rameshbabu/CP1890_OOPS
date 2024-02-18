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

    def custInfo(file_name):
        # Running the entire file will print the csv file to the console to show it's pulling
        # the data. The new issue is I have no idea how to make objects from it. I'm going to
        # push this to the GitHub, maybe Alex can figure something out before I possibly do.
        # Commit and Push in PyCharm giving me a lot of trouble getting this on my branch.
        customer_info = []
        with open(file_name) as file:
            info = csv.reader(file)
            next(file)
            for row in info:
                customer_info.append(row)
            return customer_info
    custList = custInfo("customers.csv")
    for row in custList:
        print(row)