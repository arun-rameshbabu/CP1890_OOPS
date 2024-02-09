import locale
from datetime import datetime


def get_arrival_date():
    arrival = input("Enter Arrival Date: (YYYY-MM-DD): ")
    arrival_date = datetime.strptime(arrival, "%Y-%m-%d")
    return arrival_date


def get_departure_date():
    departure = input("Enter Departure Date: (YYYY-MM-DD): ")
    departure_date = datetime.strptime(departure, "%Y-%m-%d")
    return departure_date


def get_nightly_rate(arrival_date):
    month = arrival_date, "%m"
    if month == 8:
        nightly_rate = 105
    else:
        nightly_rate = 85
    return nightly_rate


def main():
    print("The Hotel Reservation Program")
    print()
    arrival = get_arrival_date()
    departure = get_departure_date()
    print()
    night = get_nightly_rate(arrival)
    days_stayed = (departure - arrival)
    days_in = days_stayed.days
    cost = days_in * night
    locale.setlocale(locale.LC_ALL, "en-CA")
    print(f"Arrival Date: {arrival:%B %d, %Y}")
    print(f"Departure Date: {departure:%B %d, %Y}")
    print(f"Nightly rate: {locale.currency(night)}")
    print(f"Total Nights: {days_in}")
    print(f"Total Price: {locale.currency(cost)}")


print("Bye!")


if __name__ == "__main__":
    main()
