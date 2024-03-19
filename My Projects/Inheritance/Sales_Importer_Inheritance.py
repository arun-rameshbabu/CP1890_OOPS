from dataclasses import dataclass


@dataclass
class SalesItem:
    sale_date: str
    quarter: int
    # region: str
    price: float = 0.0


@dataclass
class Regions:

    def __str__(self):
        return ['west', 'south', 'east', 'north']


@dataclass
class SalesList:
    __sales_list: list

    @property
    def count(self):
        return len(self.__sales_list)

    def add_sale_item(self, sale_item: SalesItem):
        self.__sales_list.append(sale_item)

