from dataclasses import dataclass
from random import randint


@dataclass
class RandomIntList(list):
    amount: int = 0

    def create_list(self):
        for i in range(self.amount):
            num = randint(1, 100)
            self.append(num)

    def __str__(self):
        return ', '.join(map(str, list(self)))

    def get_total(self):
        total = 0
        for i, num in enumerate(list(self)):
            total += num
        return total

    def get_average(self):
        total = self.get_total()
        return '{:.3f}'.format(total / self.amount)

    def get_count(self):
        return len(list(self))


def title():
    print('Random Integer List\n')


def main():
    title()

    while True:
        try:
            amount = int(input('How many random integers should the list contain?: '))
            if amount < 0:
                print('Enter a positive integer')
                continue
            break
        except ValueError:
            print('Invalid input, please try again.')

    while True:
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
