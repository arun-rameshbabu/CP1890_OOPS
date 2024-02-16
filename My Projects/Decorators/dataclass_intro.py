from dataclasses import dataclass


class Fruit:
    __slots__ = ["name", "calories"]

    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'This is a {self.name} with {self.calories}'


banana = Fruit('Banana', 10)
banana2 = Fruit('Banana', 10)
apple = Fruit('Apple', 20)

print(apple.calories)


@dataclass(kw_only=True, frozen=True, slots=True)
class FruitD:
    name: str
    calories: float


# kw_only requires keywords when assigning
bananaD = FruitD(name='Banana', calories=10)
bananaD2 = FruitD('Banana', 10)
appleD = FruitD('Apple', 20)

print(appleD)

print(banana == banana2)
print(bananaD == bananaD2)
# frozen prevents values from changing
bananaD.calories = 60
print(bananaD.calories)
