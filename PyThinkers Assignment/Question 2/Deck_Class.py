import Card_Class
from dataclasses import dataclass, field
import random

class Deck:
    def __init__(self, cards = []):
        self.cards = cards

    def getDeck(self) :
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for suit in suits:
            for rank in ranks:
                card = Card_Class.Card(str(rank),suit)
                self.cards.append(card.getCard())

    def shuffle(self):
        random.shuffle(self.cards)

    def countCards(self):
        return f"There are {len(self.cards)} cards left in the deck"

    def dealCard(self):
        random_deal = random.randint(1,len(self.cards))
        random_deal = random_deal - 1
        return self.cards.pop(random_deal)


free = random.randint(1, 3)
print(free)


deck = Deck()
deck.getDeck()
print(deck.cards)