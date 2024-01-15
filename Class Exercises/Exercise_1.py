def calc(month, invest_2, months):
    future = 0
    for i in range(months):
        future += month
        intrest = future * invest_2
        future += intrest
        return future


def main():

    choice = "y"
    while choice == "y":
        month = int(input("Enter Monthly Investment: "))
        investment = float(input("Enter Yearly Investment Rate: "))
        year = int(input("Enter Number of Years: "))
        invest_2 = investment / (12 * 100)
        months = year * 12
        future = calc(month, invest_2, months)

        print("Monthly Investment: ", month)
        print("Interest Rate: ", investment)
        print("Years", year)
        print(f"Future Value: {future:.2f} ")

        choice = input("Continue (y/n): ")
    print("Bye!")


if __name__ == "__main__":
    main()
