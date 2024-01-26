from dataclasses import dataclass

@dataclass
class Product:
    name: str
    __price: float = 0.0  # Make 'price' private
    discountPercent: float = 0.0

    def __post_init__(self):
        self.get_price = self.__price

    def getDiscountamount(self):
        """
        Returns the discount amount.
        """
        return self.__price * (self.discountPercent/100)

    def getDiscountprice(self):
        """
        Returns the discounted price.
        """
        return self.__price * (1 - self.discountPercent/100)

    @property
    def get_price(self):
        return (self.__price)

    @get_price.setter
    def obtain_price(self, price):
        if price <= 0:
            raise ValueError("Price Cannot Be < or = 0.")
        else:
            self.__price = price