from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discount_percent: int = 0

    def get_discount_amount(self) -> float:
        return self.price * (self.discount_percent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

    def get_description(self) -> str:
        return self.name


@dataclass
class Movie(Product):
    year: int = 0

    def get_description(self) -> str:
        return f'{Product.get_description(self)}'

    def get_year(self) -> int:
        return self.year


product_1 = Product('Stanley 13 Ounce Wood Hammer', 10.00, 30)
product_2 = Product('Duct Tape, 20ft', 5.99, 20)
movie_1 = Movie('The Holy Grail - DVD', 10.00, 15, 1975)
movie_2 = Movie('Venom - BluRay', 5.00, 50, 2013)

products = [product_1, movie_1, movie_2, product_2]
for product in products:
    print('\nPRODUCT DATA')
    if isinstance(product, Movie):
        print(product.get_description())
        print(product.get_year())
        print(f'${product.get_discount_price()}')
    else:
        print(product.get_description())
        print(f'${product.get_discount_price()}')
