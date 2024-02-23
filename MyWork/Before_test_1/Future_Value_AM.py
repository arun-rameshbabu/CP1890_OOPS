# Monthly Investment / Future Value Program

import locale as lc

def month_invest():
    month = int(input("Enter monthly investment:\t"))
    return month

def year_int():
    year = float(input("Enter yearly interest rate:\t"))
    return year

def year_num():
    years = int(input("Enter number of years:\t\t"))
    return years

def total_value(month, year, years):
    total = 0
    month_int = year/(12*100)
    months = years*12
    for i in range(months):
        total += month_int
        month_int = total * month_int
        total += month_int
    return total

def main():
    while True:
        m = month_invest() #100
        y = year_int()     #12.5
        yn = year_num()    #10
        print(" ")
        lc.setlocale(lc.LC_ALL, 'en-ca')
        mi = str(lc.currency(m, grouping=True))
        print(f"Monthly investment:\t\t\t{mi}")
        print(f"Yearly interest rate: {y:13}")
        print(f"Years: {yn:28}")

        total = total_value(m, y, yn)
        totali = str(lc.currency(total, grouping=True))
        print(f"{'Future value:':21} {totali:>10}")

        cont = input("Continue? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
