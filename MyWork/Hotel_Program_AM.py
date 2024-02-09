from datetime import datetime
import locale as lc
lc.setlocale(lc.LC_ALL, 'en_CA')


def main():
    print("The Hotel Reservation Program\n")

    while True:
        while True:
            arrive = time_get("arrival")
            depart = time_get("departure")

            arrival = datetime.strptime(arrive, "%Y-%m-%d").date()
            departure = datetime.strptime(depart, "%Y-%m-%d").date()
            if arrival > departure:
                print("Arrival cannot be earlier than departure\n")
            elif arrival < departure or arrival == departure:
                break

        print(f"\nArrival Date:\t{arrival:%B %d, %Y}") # 2021-8-15
        print(f"Departure Date: {departure:%B %d, %Y}")

        nights, mes = night_rate(arrival)
        print(f"Nightly Rate:\t{lc.currency(nights)} {mes}")

        total_nights = int(departure.day - arrival.day)
        print(f"{'Total nights:'}{total_nights:4}")

        total = tot_price(total_nights, nights)
        print(f"Total price:\t{lc.currency(total, grouping=True)}")

        cont = input("\nContinue? (y/n): ").lower()
        if cont == "n":
            break
        elif cont == "y":
            continue
        else:
            print("Invalid input, ending program")
            break


def time_get(ver):
    var = ""
    if ver == "arrival":
        var = input("Enter arrival date (YYYY-MM-DD): ")
    elif ver == "departure":
        var = input("Enter departure date (YYYY-MM-DD): ")
    return var


def night_rate(arrival):
    if 6 <= arrival.month <= 8:
        night = 105.00
        message = "(High Season)"
    else:
        night = 85.00
        message = ""
    return night, message


def tot_price(total, rate):
    return float(rate * total)


if __name__ == "__main__":
    main()
