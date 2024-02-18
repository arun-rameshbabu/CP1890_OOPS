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
        self.height = int(input('Height: \t'))
        return self.height


    def get_width(self) -> int:
        self.width = int(input('Width:\t\t'))
        return self.width


    def get_perimeter(self):
        self.perimeter = (self.get_height()*2) + (self.get_width()*2)
        return self.perimeter


    def get_area(self):
        self.area = self.width * self.height
        return self.area
