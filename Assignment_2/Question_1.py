from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = ''
    last_name: str = ''
    email: str = ''

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.title()


@dataclass
class Customer(Person):
    number: str = ''


@dataclass
class Employee(Person):
    ssn: str = ''


def title():
    print('Customer/Employee Data Entry\n')


def main():
    title()
    while True:
        user_input = input('Customer or employee? (c/e): ')
        if user_input.lower() != 'e' and user_input.lower() != 'c':
            print("Please enter a valid input.")
            continue

        user = get_info(user_input)

        if isinstance(user, Customer):
            print('\nCUSTOMER')
            print(f'Name:\t\t{user.full_name}')
            print(f'Email:\t\t{user.email}')
            print(f'Number:\t\t{user.number}\n')
        else:
            print('\nEMPLOYEE')
            print(f'Name:\t\t{user.full_name}')
            print(f'Email:\t\t{user.email}')
            print(f'SSN:\t\t{user.ssn}\n')

        while True:
            cont = input('Do you want to continue? (y/n): ')
            if cont.lower() == 'y':
                print()
                break
            elif cont.lower() == 'n':
                print('\nGoodbye!')
                return
            else:
                print('Please enter a valid input.')
                continue


def get_info(user_input):
    print('\nDATA ENTRY')

    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email = input('Email: ')

    if user_input == 'c':
        number = input('Number: ')
        user = Customer(first_name=first_name, last_name=last_name, email=email, number=number)
        return user

    else:
        ssn = input("SSN: ")
        user = Employee(first_name=first_name, last_name=last_name, email=email, ssn=ssn)
        return user


if __name__ == '__main__':
    main()
