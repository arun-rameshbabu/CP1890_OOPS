"""
Assignment 1

Question 2
"""

from Classes import Deck


card_deck = Deck()
hand = []

def main():
    """
    Main code for program, calls other functions.
    """
    card_deck.shuffle()
    
    print(f"Card Dealer\n\nI have shuffled a deck of {card_deck.total()} cards.")
    
    card_num = get_cards()
    
    print("\nHere are your cards:")
    
    print_cards(card_num)
    
    print(f"\nThere are {card_deck.total()} cards left in the deck.\n\nGood Luck!")


def get_cards():
    """
    Obtains the number of cards the player/user wants.

    Returns
    -------
    choice : int
        Number of cards to give to the player/user.
    """
    while True:
        try:
            while True:
                choice = int(input("\nHow many cards would you like?: "))
                if choice < 1 or choice > card_deck.total():
                    print(f"Must take atleast 1 card, and no more than the deck total ({card_deck.total()}).")
                else:
                    break
            return choice
        except ValueError:
            print("Invalid entry, try again.")


def print_cards(num):
    """
    Takes cards from the deck and puts them in the player/user's hand.
    Prints the name of each card that the player/user receives.

    Parameters
    ----------
    num : int
        Number of cards to give to the player/user.
    """
    while num > 0:
        hand.append(card_deck.Deck.pop(0))
        print(hand[-1].cardName())
        num -= 1


if __name__ == "__main__":
    main()
