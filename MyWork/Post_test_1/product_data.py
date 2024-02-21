from inheritance import Product, Book
from dataclasses import dataclass


@dataclass
class Movie(Product):
    year: int = 0
    format: str = ""

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} - {self.format}"


def main():
    title = ("Product Data").upper()
    title2 = f"{title}\nName:"

    Product1 = Product("Stanley 13 Ounce Wood Hammer", 9.99, 50.6)
    Product2 = Movie("The Holy Grail", 9.99, 52, 1975, "DVD")
    Product3 = Book("The Shining", 12.99, 10, "Stephen King")

    print(f"{title2:32} {Product1.getDescription():42}\nDiscount price: {Product1.getDiscountPrice():8.2f}\n")
    print(f"{title2:32} {Product2.getDescription():42}\nYear: {Product2.year:18}\nDiscount price: {Product2.getDiscountPrice():8.2f}\n")
    print(f"{title2:32} {Product3.getDescription():42}\nAuthor: {Product3.author:>24}\nDiscount price: {Product3.getDiscountPrice():9.2f}")


if __name__ == "__main__":
    main()
