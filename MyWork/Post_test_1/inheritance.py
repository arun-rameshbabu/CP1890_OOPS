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
    discountPercent: float = 0.0

    def getDiscountAmount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self) -> float:
        return self.price - self.getDiscountAmount()

    def getDescription(self) -> str:
        return self.name


@dataclass
class Book(Product):
    author: str = ''

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

    print(f"{product1.getDescription()}{product1.getDiscountPrice():26.2f}")
    print(f"{book1.getDescription()}{book1.getDiscountPrice():14.2f}")
    print(f"{movie1.getDescription()}{movie1.getDiscountPrice():30.2f}")


if __name__ == "__main__":
    main()
