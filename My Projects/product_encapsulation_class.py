class Product:

    def __init__(self, p_name='', p_price=0.0, discount_per=0):
        self.name: str = p_name
        self.__price: float = p_price
        self.discount_percent: int = discount_per

    def get_discount_amount(self):
        return self.__price * (self.discount_percent / 100)

    def get_discount_price(self):
        return self.__price - self.get_discount_amount()

    def __post_init__(self):
        self.p_price = self.__price

    @property
    def price(self):
        return float(self.__price)

    @price.setter
    def price(self, p_price):
        if p_price <= 0:
            raise ValueError("Price cannot be less than 0")
        else:
            self.__price = p_price
