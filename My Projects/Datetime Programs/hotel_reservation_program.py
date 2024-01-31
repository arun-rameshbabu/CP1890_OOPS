from datetime import datetime


def title():
    print('The Hotel Reservation Program\n')


def get_arrival_departure():
    arrival_date = input('Enter arrival date (YYYY-MM-DD): ')
    departure_date = input('Enter departure date (YYYY-MM-DD): ')
    return datetime.strptime(arrival_date, '%Y-%m-%d'), datetime.strptime(departure_date, '%Y-%m-%d')


def display_reservation(arrival_date, departure_date):
    print('\nArrival Date:\t', arrival_date)
    print('Departure Date:\t', departure_date)
    print('Nightly rate:\t$105.00 (High season)')
    print(f'Total nights:\t{departure_date - arrival_date}')
    print(f'Total price:\t${(departure_date - arrival_date) * 105.00}')


def main():
    title()
    while True:
        arrival, departure = get_arrival_departure()
        display_reservation(arrival, departure)

        loop = input('\nContinue? (y/n): ')
        if loop == 'n':
            break


if __name__ == '__main__':
    main()
    print('\nBye!')
