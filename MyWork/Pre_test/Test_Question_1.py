
class Rectangle:
    def __init__(self, length, width):
        """
        This function initializes the class attributes.
        :param length: rectangle length
        :param width: rectangle width
        """
        self.length = length
        self.width = width
        if self.length == self.width:
            self.__is_square = True
        else:
            self.__is_square = False

    @property
    def area(self):
        """
        This function returns the area of the rectangle.
        :return a: rectangle area
        """
        a = self.width * self.length
        if a < 0:
            a = a * (-1)
        return a

    @property
    def perimeter(self):
        """
        This function returns the perimeter of the rectangle.
        :return: rectangle perimeter
        """
        w = self.width * 2
        l = self.length * 2

        if w < 0:
            w = 0
        if l < 0:
            l = 0

        return l + w

    @property
    def is_square(self):
        """
        This function gets the is_square attribute.
        :return self.__is_square: Bool value for whether the rectangle is a square or not.
        """
        return self.__is_square


def main():
    """
    Test values for class.
    """
    rect1 = Rectangle(5, 5)
    rect2 = Rectangle(6, 8)
    rect3 = Rectangle(-4, 4)

    print(rect1.area)
    print(rect1.perimeter)
    print(rect1.is_square, "\n")

    print(rect2.area)
    print(rect2.perimeter)
    print(rect2.is_square, "\n")

    print(rect3.area)
    print(rect3.perimeter)
    print(rect3.is_square, "\n")


if __name__ == "__main__":
    main()
