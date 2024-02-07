import datetime


def get_arrival_date():
    arrival = input("Enter Arrival Date: (YYYY/MM/DD): ")
    arrival_date = datetime.datetime.strptime(arrival, "%B %d, %Y")
    return arrival_date


def get_departure_date():
    departure = input("Enter Departure Date: (YYYY/MM/DD): ")
    departure_date = datetime.datetime.strptime(departure, "%B %d, %Y")
    return departure_date


def main():
    print("The Hotel Reservation Program")


if __name__ == "__main__":
    main()
