import Card_Class
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
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
        print('I have shuffled a deck of 52 cards')

    def countCards(self):
        return f"There are {len(self.cards)} cards left in the deck."

    def dealCard(self, num:int):
        for i in range(num):
            card = self.cards.pop()
            print(card.getCard())

