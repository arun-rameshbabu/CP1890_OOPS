class Product:
    def __init__(self, name = "", price =0.0, discount_percent=0)
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

        def getDiscountamount(self):
            """
            Returns the
            :return:
            """
            return self.price * (self.discountPercent / 100)

        def getDiscountprice(self):
            return self.price - self.getDiscountamount()
