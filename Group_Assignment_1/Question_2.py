"""
Assignment 1

Question 2
"""

from Classes import Card, Deck

card_deck = Deck.createDeck(Card)

def main():
    print(f"Card Dealer\n\nI have shuffled a deck of {card_deck.cardNum()} cards.")
    
    choice = int(input("\nHow many cards would you like?: "))
    
    print("Here are your cards:")

if __name__ == "__main__":
    main()