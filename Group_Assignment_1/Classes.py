"""
Assignment 1

Classes
"""

from dataclasses import dataclass
import random


@dataclass
class Card:
    """
    Playing Card with Rank and Suit
    """
    rank:str = ""
    suit:str = ""
    
    def cardName(self):
        """
        Returns
        -------
        str
            Full name of card ex:
                'Ace of Hearts'.
        """
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Deck of Playing Cards
    """
    def __init__(self):
        self.deckCards = []
    
    def createDeck(self):
        """
        Generates deck.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.deckCards.append(card)
    
    @property
    def shuffleDeck(self):
        random.shuffle(self.deckCards)
        
    @property
    def cardNum(self):
        return f"{len(self.deckCards)}"
    