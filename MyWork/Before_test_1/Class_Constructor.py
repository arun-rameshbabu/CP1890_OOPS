class Product:
    def __init__(self, name = "", price=0.0, discount_percent = 0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

        def get_discountAmount(self):
            return self.price * (self.discountPercent / 100)

        def get_discountPrice(self):
            return self.price - self.get_discountAmount()