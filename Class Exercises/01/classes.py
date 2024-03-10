from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    discountPercent: int

    def getDiscountamount(self):
        """
        Returns the
        :return:
        """
        return self.price * (self.discountPercent/100)

    def getDiscountprice(self):
        return self.price - self.getDiscountamount()
