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

    def __str__(self):
        return self.name + " is actually Thor's hammer."

    def __eq__(self, other):
        return self.name == other.name


product1 = Product("Stanley 13 Ounce Wood Hammer", 9.99, 50.6)
print(str(product1))  # <- Default: Product(name='Stanley 13 Ounce Wood Hammer', price=9.99, discountPercent=50.6)
# print(dir(product1))

product2 = Product("Stanley 13 Ounce Wood Hammer", 6.00, 20)

print(product1 == product2)  # <- Default: False
