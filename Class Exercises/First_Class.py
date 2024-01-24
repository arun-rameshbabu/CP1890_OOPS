from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    __price: float = 0.0
    discount_percent: float = 0.0

    def get_discount_amount(self) -> float:
        return self.__price * self.discount_percent / 100

    def get_discount_price(self) -> float:
        return self.__price * self.get_discount_amount()

    def __post_init__(self):
        self.price = self.__price

    @property
    def get_value(self) -> float:
        return self.__price

    @get_value.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be less than 0")
        else:
            self.__price = price

    def getDiscountAmount(self):
        return self.price * (self.get_discount_precent / 100)

    def getDiscountPercent(self):
        return self.price - self.getDiscountAmount()