"""
Assignment 1

Classes
"""

from dataclasses import dataclass
import random


# Question 2:
@dataclass
class Card:
    rank:str = ""
    suit:str = ""
    
    def cardName(self):
        """
        Gives the name of the card ex: 'Ace of Spades'.
        
        Returns
        -------
        str
            Name of card.
        """
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        """
        Creates 'Deck' list and uses '__create()' to fill said deck with cards.
        """
        self.Deck = []
        self.__create()
        
    def __create(self):
        """
        Creates the deck.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.Deck.append(card)
    
    def shuffle(self):
        """
        Shuffles the deck.
        """
        random.shuffle(self.Deck)
    
    def total(self):
        """
        Returns the number of cards in the deck.
        """
        return int(len(self.Deck))


# Question 1
@dataclass
class Rectangle:
    height: int = 0
    width: int = 0
    perimeter: int = 0
    area: int = 0

    def get_height(self) -> int:
        """
        Gets height of rectangle from user.

        Returns
        -------
        int
            Rectangle height.
        """
        self.height = int(input('Height: \t'))
        return self.height

    def get_width(self) -> int:
        """
        Gets width of rectangle from user.

        Returns
        -------
        int
            Rectangle width.
        """
        self.width = int(input('Width:\t\t'))
        return self.width

    def get_perimeter(self):
        """
        Gets perimeter of rectangle.

        Returns
        -------
        int
            Rectangle perimeter.
        """
        self.perimeter = (self.get_height()*2) + (self.get_width()*2)
        return self.perimeter

    def get_area(self):
        """
        Gets area of rectangle.

        Returns
        -------
        int
            Rectangle area.
        """
        self.area = self.width * self.height
        return self.area
    
    def create(self):
        """
        Prints string representation of the rectangle.
        """
        space=" "
        for i in range(self.height):
            if i == 0 or i == self.height-1:
                print("* " * self.width)
            else:
                print('*' + (space*(self.width-2))*2 + ' *')


# Question 3:
@dataclass
class Customer:
    custid:int
    firstName:str
    lastName:str
    company:str
    address:str
    city:str
    state:str
    zipCode:str

    def custNameAddress(self):
        """
        Returns an f-string with customer information.

        Returns
        -------
        str
            Customer name and address info.
        """
        fullAddress = f"{self.address}\n" + f"{self.city}" + ", " + f"{self.state}" + f" {self.zipCode}"
        fullName = f"{self.firstName}" + " " + f"{self.lastName}"
        if self.company == "":
            return f"{fullName}\n{fullAddress}"
        else:
            return f"{fullName}\n{self.company}\n{fullAddress}"
