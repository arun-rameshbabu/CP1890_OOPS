"""
Assignment 1

Question 2
"""

import random


Deck = []


def main():
    cards(Deck)
    print(f"Card Dealer\n\nI have shuffled a deck of {len(Deck)} cards.")
    
    card_num = get_cards(Deck)
    
    print("\nHere are your cards:")
    
    random.shuffle(Deck)
    
    print_cards(card_num, Deck)
    
    print(f"\nThere are {len(Deck)} cards left in the deck.\n\nGood Luck!")
    

def cards(Deck):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    for suit in suits:
        for rank in ranks:
            card = [rank, suit]
            Deck.append(card)


def get_cards(Deck):
    while True:
        try:
            while True:
                choice = int(input("\nHow many cards would you like?: "))
                if choice < 1 or choice > len(Deck):
                    print(f"Must take atleast 1 card, and no more than the deck total ({len(Deck)}).")
                else:
                    break
            return choice
        except ValueError:
            print("Invalid entry, try again.")


def print_cards(num, Deck):
    hand = []
    
    while num > 0:
        hand.append(Deck.pop(0))
        print(f"{hand[-1][0]} of {hand[-1][1]}")
        num -= 1


if __name__ == "__main__":
    main()
