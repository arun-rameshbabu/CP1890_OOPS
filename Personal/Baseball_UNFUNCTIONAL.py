from datetime import date
import Baseball_Class_UNFUNCTIONAL

def get_game_date():
    game_date = date(2021,3,21)
    return game_date

def days_till_game():
    print("Filler text")

def main():
    print('=' * 50)
    print(f"{'Baseball Team Manager':15}")
    print()
    print("CURRENT DATE: {}".format(date.today()))
    print("GAME DATE: {}".format(get_game_date()))





if __name__ == "__main__":
    main()
