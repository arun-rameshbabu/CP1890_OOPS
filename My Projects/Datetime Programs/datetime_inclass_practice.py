from datetime import datetime, timedelta


def title():
    print("The Invoice Due Date Program\n")


def get_invoice_date():
    while True:
        invoice_date = input('Enter the invoice date (MM/DD/YY): ')
        try:
            return datetime.strptime(invoice_date, "%m/%d/%y")
        except ValueError:
            print('Invalid entry for invoice date.\n')


def get_due_date(invoice_due_date):
    due_date = invoice_due_date + timedelta(days=30)
    return due_date


def main():
    title()
    while True:
        invoice_date = get_invoice_date()
        due_date = get_due_date(invoice_date)

        print()
        print(f'Invoice Date:\t{invoice_date: %B %d, %Y}')
        print(f'Due Date:\t\t{due_date: %B %d, %Y}')
        print(f'Current Date:\t{datetime.today(): %B %d, %Y}')

        if datetime.today() > due_date:
            overdue = datetime.today() - due_date
            print(f'\nInvoice is {overdue.days} day(s) overdue.')
        else:
            print('\nInvoice is not due yet.')

        option = input('\nContinue? (y/n): ')
        if option == 'n':
            break
        elif option == 'y':
            print()


if __name__ == '__main__':
    main()
    print('\nBye!')