from Deck_Class import Deck

def main():
    print("Card Dealer")
    print()
    deck = Deck()
    deck.getDeck()
    deck.shuffle()
    print()
    cards_amount = int(input("How many cards would you like?   "))
    print()
    print("Here are your Cards:")
    deck.dealCard(cards_amount)
    print()
    print(deck.countCards())
    print()
    print("Good luck!")



if __name__ == "__main__":
    main()