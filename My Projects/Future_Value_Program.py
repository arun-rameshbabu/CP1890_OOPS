import locale as l
l.setlocale(l.LC_ALL, 'en-ca')


def get_monthly_investment():
    monthly_investment = float(input("Enter monthly investment: \t\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate: \t"))
    num_years = int(input("Enter number of years: \t\t\t"))
    return monthly_investment, yearly_interest_rate, num_years


def calc_future_value(monthly_investment, yearly_interest_rate, num_years):
    future_value = 0
    for i in range(num_years * 12):
        future_value += monthly_investment
        monthly_interest = (future_value * (yearly_interest_rate / (12*100)))
        future_value += monthly_interest
    return future_value


def main():
    while True:
        monthlyinv, yearlyint, numyears = get_monthly_investment()
        f_value = calc_future_value(monthlyinv, yearlyint, numyears)
        print()
        print(f"Monthly investment: {l.currency(monthlyinv, grouping=True):>15}")
        print(f"Interest rate: {yearlyint:>20}")
        print(f"Years: {numyears:>28}")
        print(f"Future Value: {l.currency(f_value, grouping=True):>21}")

        option = input("\nContinue? (y/n): ")
        if option == "n":
            print('\nBye!')
            break


if __name__ == "__main__":
    main()



