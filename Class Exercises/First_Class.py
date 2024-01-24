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

    @property
    def get_value(self) -> float:
        return self.__price