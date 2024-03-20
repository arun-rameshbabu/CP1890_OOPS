from dataclasses import dataclass
from random import randint


@dataclass
class RandomIntList(list):
    amount: int = 0

    def create_list(self):
        # Adds a list of random numbers depending on the amount attribute
        for i in range(self.amount):
            num = randint(1, 100)
            self.append(num)

    def __str__(self):
        # Returns the list in a readable string format where each item in the list is separated by a comma.
        return ', '.join(map(str, list(self)))

    def get_total(self):
        # Calculates the total by adding each number in the list
        total = 0
        for num in list(self):
            total += num
        return total

    def get_average(self):
        # Calculates the average by grabbing the total and dividing it by the amount of integers
        total = self.get_total()
        return '{:.3f}'.format(total / self.amount)

    def get_count(self):
        # Returns the length of the list
        return len(list(self))


def title():
    print('Random Integer List\n')


def main():
    title()

    while True:
        # Gets users desired amount of integers and validates the input
        try:
            amount = int(input('How many random integers should the list contain?: '))
            if amount <= 0:
                print('Enter a positive integer')
                continue
            break
        except ValueError:
            print('Invalid input, please try again.')

    while True:
        # Displays result and allows user to replay as many times as they want.
        int_list = RandomIntList(amount)
        int_list.create_list()
        print("\nRandom Integers")
        print("===============")
        print(f"Integers:\t{int_list}")
        print(f"Count:\t\t{int_list.get_count()}")
        print(f"Total:\t\t{int_list.get_total()}")
        print(f"Average:\t{int_list.get_average()}")

        while True:
            user_input = input("\nContinue? (y/n): ")
            if user_input.lower() == 'y':
                break
            elif user_input.lower() == 'n':
                print("\nBye!")
                return
            else:
                print("Invalid input, please try again.")
                continue


if __name__ == '__main__':
    main()
