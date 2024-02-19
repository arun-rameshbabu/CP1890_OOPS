from inheritance import Product, Book
from dataclasses import dataclass


@dataclass
class Movie(Product):
    format: str = ""

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} - {self.format}"


def main():
    title = ("Product Data").upper()
    title2 = f"{title}\nName:"

    Product1 = Product("Stanley 13 Ounce Wood Hammer", 9.99, 49.4)
    Product2 = Movie("The Holy Grail", 9.99, 48, "DVD")
    Product3 = Book("The Shining", 12.99, 90, "Stephen King")

    print(f"{title2:32} {Product1.getDescription():42}\nDiscount price: {Product1.getDiscountAmount():8.2f}\n")
    print(f"{title2:32} {Product2.getDescription():42}\nDiscount price: {Product2.getDiscountAmount():8.2f}\n")
    print(f"{title2:32} {Product3.getDescription():42}\nDiscount price: {Product3.getDiscountAmount():8.2f}")


if __name__ == "__main__":
    main()
