"""
    Product
name
price
discountamount <- discountpercent
--------------------
getdiscountamount()
getdiscountprice()
getdescription

    Book
author
--------------------
getdescription

    Movie
year
--------------------
getdescription
"""

from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    discountPercent: float = 0

    def getDiscountAmount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self) -> float:
        return self.price - self.getDiscountAmount()

    def getDescription(self) -> str:
        return self.name

"""
@dataclass
class Book(Product):
    author: str = ''

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} by {self.author}"
"""

class Book(Product):
    def __init__(self, name='', price=0.0, discountPercent=0, author=''):
        Product.__init__(self, name, price, discountPercent)

        self.author = author

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} by {self.author}"

@dataclass
class Movie(Product):
    year: int = 0

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} {self.year}"


def main():
    product1 = Product("Quartet Marker", 2.99, 20)
    book1 = Book("The Shining", 12.99, 10, "Stephen King")
    movie1 = Movie("Venom", 12.99, 25, 2013)

    print(f"{product1.getDescription():30} ${product1.getDiscountPrice():5.2f}")
    print(f"{book1.getDescription():30} ${book1.getDiscountPrice():5.2f}")
    print(f"{movie1.getDescription():30} ${movie1.getDiscountPrice():5.2f}")

    print("")
    print(isinstance(movie1, Movie))
    print(isinstance(movie1, Product))
    print(isinstance(movie1, Book))


if __name__ == "__main__":
    main()
