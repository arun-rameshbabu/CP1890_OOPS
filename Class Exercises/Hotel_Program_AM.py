from datetime import datetime


def main():
    print("The Hotel Reservation Program\n")


    while True:
        arrive = time_get("arrival")
        depart = time_get("departure")

        arrival = datetime.strptime(arrive, "%Y-%m-%d").date()
        departure = datetime.strptime(depart, "%Y-%m-%d").date()

        print(f"\nArrival Date: {arrival:%B %d, %Y}")
        print(f"Departure Date: {departure:%B %d, %Y}")

        print(f"Nightly Rate: {night_rate(arrival)}")

        total_nights = int(departure.day - arrival.day)
        print("Total nights: ", total_nights)

        total = tot_price(total_nights, night_rate(arrival))
        print(f"Total price: {int(total)}.00")

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
    if arrival.month >= 6 and arrival.month <= 9:
        night = "$105.00 (High season)"
    else:
        night = "$85.00"
    return night


def tot_price(total, rate):
    tot = 0.0
    if rate == "$105.00 (High season)":
        tot = 105.00
    elif rate == "$85.00":
        tot = 85.00
    return float(tot * total)


if __name__ == "__main__":
    main()
