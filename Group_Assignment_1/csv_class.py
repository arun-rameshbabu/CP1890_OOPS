from dataclasses import dataclass

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
        self.fullAddress = state + ", " + city + ", " + address + ", " + zipCode
        self.fullName = firstName + " " + lastName

    def custInfo(self):
        return self.fullName, self.fullAddress
