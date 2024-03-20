from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = ''
    last_name: str = ''
    email_address: str = ''

    @property
    def full_name(self) -> str:
        return self.first_name + ' ' + self.last_name


@dataclass
class Customer(Person):
    customer_number: str = ''


@dataclass
class Employee(Person):
    social_security_number: str = ''


# Takes inputs and returns a Customer object
def customer_creation():
    print("\nDATA ENTRY")
    f_name = str(input("First name: "))
    l_name = str(input("Last name: "))
    email = str(input("Email: "))
    c_number = str(input("Number: "))

    customer = Customer(f_name, l_name, email, c_number)
    return customer


# Takes inputs and returns an Employee object
def employee_creation():
    print("\nDATA ENTRY")
    f_name = str(input("First name: ")).capitalize()
    l_name = str(input("Last name: ")).capitalize()
    email = str(input("Email: ")).lower()
    e_ssn = str(input("SSN: "))

    employee = Employee(f_name, l_name, email, e_ssn)
    return employee


def main():
    loop = 'y'
    print("Customer/Employee Date Entry")
    while loop == 'y':
        c_or_e = str(input("\nCustomer or employee? (c/e): ")).lower()

        if c_or_e == 'c':
            person = customer_creation()
        elif c_or_e == 'e':
            person = employee_creation()
        else:
            print("Invalid input, try again.")
            continue

# Checks to see if the person variable is an Employee or Customer
        if isinstance(person, Customer):
            print("\nCUSTOMER")
            print(f"Name:\t{person.full_name}")
            print(f"Email:\t{person.email_address}")
            print(f"Number:\t{person.customer_number}")
        elif isinstance(person, Employee):
            print("\nEMPLOYEE")
            print(f"Name:\t{person.full_name}")
            print(f"Email:\t{person.email_address}")
            print(f"SSN:\t{person.social_security_number}")

# Loop used to get an appropriate input
        while loop != 'n':
            loop = input("\nContinue? (y/n): ").lower()
            if loop == "y":
                break
            elif loop == "n":
                print("\nBye!")
            else:
                print("Invalid input, try again.")


if __name__ == "__main__":
    main()
    