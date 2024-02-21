from inheritance_basics import Product
from override_Dice_Roller_Class import Die, Dice
from Subclasses import CustomRequestError

# product1 = Product('Stanley 13 Ounce Wood Hammer', 5.489, 10)
# print(str(product1))
# print()
#
# product2 = Product('Stanley 13 Ounce Wood Hammer', 6.00, 20)
#
# print(product1 == product2)
#
# dice = Dice()
# dice.add_die(Die(6))
# dice.add_die(Die(3))
# dice.add_die(Die(2))
# dice.add_die(Die(6))
# dice.add_die(Die(3))
# dice.add_die(Die(2))
# dice.add_die(Die(6))
# dice.add_die(Die(3))
#
# for die in dice:
#     die.roll()
#     print(str(die))


def read_movies():
    try:
        movies = []
        with open('movies.csv') as file_movies:
            pass
    except FileNotFoundError:
        raise CustomRequestError("This is my error")
    except Exception:
        raise CustomRequestError("This is a generic error")


try:
    movies = read_movies()
except CustomRequestError as e:
    print("CustomRequestError:", e)
