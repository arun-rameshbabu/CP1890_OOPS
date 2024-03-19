from dataclasses import dataclass


@dataclass
class Rectangle:
    length: int
    width: int
    __is_square: bool = False

    @property
    def area(self):
        if self.length > 0:
            if self.width > 0:
                return self.width * self.length
            else:
                return (self.width * -1) * self.length
        else:
            if self.width > 0:
                return self.width * (self.length * -1)
            else:
                return 0

    @property
    def perimeter(self):
        if self.length > 0:
            if self.width > 0:
                return 2 * (self.width + self.length)
            else:
                return 2 * self.length
        else:
            if self.width > 0:
                return 2 * self.width
            else:
                return 0

    @property
    def is_square(self):
        if self.width == self.length:
            self.__is_square = True
            return self.__is_square
        else:
            self.__is_square = False
            return self.__is_square


def main():
    rect1 = Rectangle(5, 5)
    rect2 = Rectangle(6, 8)
    rect3 = Rectangle(-4, 4)

    print(rect1.area)
    print(rect1.perimeter)
    print(rect1.is_square)
    print()

    print(rect2.area)
    print(rect2.perimeter)
    print(rect2.is_square)
    print()

    print(rect3.area)
    print(rect3.perimeter)
    print(rect3.is_square)


if __name__ == "__main__":
    main()
