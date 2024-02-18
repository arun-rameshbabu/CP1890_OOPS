import Card_Class

ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
suits = ['Clubs','Diamonds','Hearts','Spades']

@dataclass
class Deck:
    cards:list = []

    def getDeck(self) -> list:
        for rank in ranks:
            for suit in suits:
                card = Card_Class.Card(rank,suit)
                self.cards.append(card.getCard())