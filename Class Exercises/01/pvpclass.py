from dataclasses import dataclass

@dataclass
class Product:
    name: str
    __price: float = 0.0  # Make 'price' private
    discountPercent: float = 0.0

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