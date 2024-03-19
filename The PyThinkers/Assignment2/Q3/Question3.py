from dataclasses import dataclass


@dataclass
class Animal:
    """
    Instantiates a class called Animal that has a name and species attribute
    and a method to print the animal's sound
    """
    name: str = ''
    species: str = ''

    def speak(self):
        # prints the sound of the animal
        print("Sound")


@dataclass
class Dog(Animal):
    """
    Instantiates a subclass called Dog of the Animal superclass that has a name, species, and an additional breed
    attribute and a method to print the sound a dog makes
    """
    breed: str = ''

    def speak(self):
        # prints the sound of a Dog
        print('Woof!')


@dataclass
class Cat(Animal):
    """
    Instantiates a subclass called Dog of the Animal superclass that has a name, species, and an additional breed
    attribute and a method to print the sound a dog makes
    """
    color: str = ''

    def speak(self):
        # prints the sound of a Cat
        print('Meow!')


dog = Dog("Max", "Dog", "Golden Retriever")
cat = Cat("Whiskers", "Cat", "Orange")
print("Dog:")
print("Name:", dog.name)
print("Species:", dog.species)
print("Breed:", dog.breed)
print("Sound:", end=" ")
dog.speak()
print("\n")
print("Cat:")
print("Name:", cat.name)
print("Species:", cat.species)
print("Color:", cat.color)
print("Sound:", end=" ")
cat.speak()
