from dataclasses import dataclass
import csv


@dataclass
class Customer:
    id: int = 0
    firstName: str = ''
    lastName: str = ''
    company: str = ''
    address: str = ''
    city: str = ''
    state: str = ''
    zip: str = ''

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def fullAddress(self):
        if self.company == '':
            return f"{self.address} \n{self.city}, {self.state} {self.zip}"
        else:
            return f"{self.company} \n{self.address} \n{self.city}, {self.state} {self.zip}"


def getCustomers():
    with open('customers.csv', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
