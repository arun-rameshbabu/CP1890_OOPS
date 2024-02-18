import Card_Class
from dataclasses import dataclass, field

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


deck = Deck()
deck.getDeck()
print(deck.cards)