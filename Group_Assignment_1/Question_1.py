from Classes import Rectangle


def title():
    print("Rectangle Calculator")
    print()


def main():
    title()

    loop = True

    while loop:
        rectangle = Rectangle()

        print(f'Perimeter:  {rectangle.get_perimeter()}')
        print(f'Area:  \t\t{rectangle.get_area()}')

        space=" "

        for i in range(rectangle.height):
            if i == 0 or i == rectangle.height-1:
                print("*" * rectangle.width)
            else:
                print('*' + space*(rectangle.width-2) + '*')

        again = input("\nContinue? (y/n): ").lower()

        if again == 'y':
            loop = True
        elif again == 'n':
            loop = False

    print("\nBye!")


if __name__ == "__main__":
    main()