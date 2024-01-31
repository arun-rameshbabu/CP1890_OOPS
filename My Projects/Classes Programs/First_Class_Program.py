from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discountPercent: int

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()


product1 = Product("Stanley Hammer", 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 19.50, 30)
product3 = Product('Economy Duct Tape, 60 yds, Silver', 9.99, 100)


def title():
    print("\nThe Product Viewer program\n")


def listProducts():
    print("PRODUCTS")
    print(f"1. {product1.name}")
    print(f"2. {product2.name}")
    print(f"3. {product3.name}")


def showProductData(productNumber):
    print("\nPRODUCT DATA")
    print(f"Name:\t\t\t\t {productNumber.name:}")
    print(f"Price:\t\t\t\t {productNumber.price:}")
    print(f"Discount percent:\t {productNumber.discountPercent:d}%")
    print(f"Discount amount:\t {productNumber.getDiscountAmount():.2f}")
    print(f"Discount price:\t\t {productNumber.getDiscountPrice():.2f}")


def main():
    title()
    listProducts()
    while True:
        option = int(input("\nEnter product number: "))
        if option == 1:
            showProductData(product1)
        elif option == 2:
            showProductData(product2)
        elif option == 3:
            showProductData(product3)

        loop = input("\nView another product? (y/n): ")
        if loop == "n":
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
