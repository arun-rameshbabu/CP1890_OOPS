import locale as lc


def values():
    monthly = int(input("Enter monthly investment:\t "))
    interest = float(input("Enter yearly interest rate:\t "))
    years = int(input("Enter number of years: \t\t "))
    return monthly, interest, years


def calc(monthly, interest, years):
    future = 0
    for i in range(years*12):
        future += monthly
        month_int = future * (interest/(12*100))
        future += month_int
    return future


def main():
    while True:
        monthly, interest, years = values()
        future = calc(monthly, interest, years)
        lc.setlocale(lc.LC_ALL, 'en-ca')
        print(f"\nMonthly investment:\t {lc.currency(monthly, grouping=True):>30}")
        print(f"Interest rate:\t\t {interest:>30}")
        print(f"Years:\t\t\t\t {years:>30}")
        print(f"Future value:\t\t {lc.currency(future, grouping=True):>30}")

        option = input('\nContinue? (y/n): ')
        if option == 'n':
            break


if __name__ == "__main__":
    main()