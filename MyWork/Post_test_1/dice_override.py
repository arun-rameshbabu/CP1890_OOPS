from Inheritance_Dice_Roller_Classes import Die, Dice

dice = Dice()
dice.addDie(Die(6))
dice.addDie(Die(3))
dice.addDie(Die(2))

for die in dice:
    print(die)


print("")

from Subclasses import CustomRequestError


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
    print("CustomRequestError", e)
