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


def getCustomers(object_list):
    with open('customers.csv', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            object_list.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def title():
    print("Customer Viewer")

def main():
    object_list = []
    getCustomers(object_list)
    title()
    loop = 'y'
    while loop.lower() == 'y':
        cust_id = input('\nEnter customer ID: ')
        access = False
        for obj in object_list:
            if cust_id == obj.id:
                print()
                print(obj.fullName)
                print(obj.fullAddress)
                loop = input('\nContinue? (y/n): ')
                while loop.lower() != 'y' and loop.lower() != 'n':
                    print('Please enter "y" or "n".')
                    loop = input('\nContinue? (y/n): ')
                access = True
        if access == False:
            print("\nNo customer with that ID")
            loop = input('\nContinue? (y/n): ')
            while loop.lower() != 'y' and loop.lower() != 'n':
                print('Please enter "y" or "n".')
                loop = input('\nContinue? (y/n): ')
    print("\nBye!")


if __name__ == '__main__':
    main()