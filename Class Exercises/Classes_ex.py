from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price:float
    discountPercent:int

    def get_discountAmount(self):
        return self.price * (self.discountPercent /100)

    def get_discountPrice(self):
        return self.price - self.get_discountAmount()