from dataclasses import dataclass


@dataclass
class Animal:
    name: str = ''
    species: str = ''

    def speak(self):
        sound = ''
        return sound


@dataclass
class Dog(Animal):
    breed: str = ''

    def speak(self):
        sound = Animal.speak(self) + "Woof!"
        print(sound)

@dataclass
class Cat(Animal):
    color: str = ''

    def speak(self):
        sound = Animal.speak(self) + "Meow!"
        print(sound)


dog = Dog("Max", "Dog", "Golden Retriever")
cat = Cat("Whiskers", "Cat", "Orange")

print("Dog:")
print("Name:", dog.name)
print("Species:", dog.species)
print("Breed:", dog.breed)
print("Sound:", end=" ")
dog.speak()

print()

print("Cat:")
print("Name:", cat.name)
print("Species:", cat.species)
print("Color:", cat.color)
print("Sound:", end=" ")
cat.speak()
