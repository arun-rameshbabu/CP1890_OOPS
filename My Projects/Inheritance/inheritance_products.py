from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discount_percent: int = 0
