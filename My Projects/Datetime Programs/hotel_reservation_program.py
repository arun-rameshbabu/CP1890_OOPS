from datetime import datetime
import locale


def title():
    print('The Hotel Reservation Program\n')


def get_arrival_date():
    while True:
        arrival_date = input('Enter arrival date (YYYY-MM-DD): ')
        try:
            arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d')
        except ValueError:
            print('Invalid date entered.')
            continue

        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print('Invalid date entered. Must be today or later.')
        else:
            return arrival_date


def get_departure_date(arrival_date):
    while True:
        departure_date = input('Enter departure date (YYYY-MM-DD): ')
        try:
            departure_date = datetime.strptime(departure_date, '%Y-%m-%d')
        except ValueError:
            print('Invalid date entered.')
            continue

        if departure_date <= arrival_date:
            print('Invalid date entered. Must be later than arrival date.')
        else:
            return departure_date


def display_reservation(arrival_date, departure_date, rate, rate_message):
    date_format = '%B %d %Y'
    locale.setlocale(locale.LC_ALL, 'en_CA')

    print(f'\nArrival Date:\t{arrival_date:{date_format}}')
    print(f'Departure Date:\t{departure_date:{date_format}}')
    print(f'Nightly rate:\t{locale.currency(rate)} {rate_message}')
    print(f'Total nights:\t{(departure_date - arrival_date).days}')
    print(f'Total price:\t{locale.currency(rate * (departure_date - arrival_date).days)}')


def main():
    title()
    while True:
        arrival = get_arrival_date()
        departure = get_departure_date(arrival)

        if arrival.month == 8:
            rate = 105
            rate_message = '(High season)'
        else:
            rate = 85.0
            rate_message = ''

        display_reservation(arrival, departure, rate, rate_message)

        loop = input('\nContinue? (y/n): ')
        if loop == 'n':
            break


if __name__ == '__main__':
    main()
    print('\nBye!')
