from Deck_Class import Deck


def cardsAmount() -> int:
    """

    :return: int
    """
    while True:  # handles value error
        try:
            cards_ammount = int(input("How many cards would you like? :  "))
            return cards_ammount
            break
        except ValueError:
            print('Invalid input!')


def main():
    print("Card Dealer")
    print()
    deck = Deck()  # constructs the deck object
    deck.getDeck()  # adds the cards to the deck
    deck.shuffle()  # shuffles the deck
    print()
    cards_amount = cardsAmount()
    print()
    print("Here are your Cards:")
    deck.dealCard(cards_amount)
    print()
    print(deck.countCards())
    print()
    print("Good luck!")


if __name__ == "__main__":
    main()
