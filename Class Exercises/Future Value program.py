#!
'''
Date: 01/12/2024
Name: Michael Agonsi
'''
import locale as lc
lc.setlocale(lc.LC_ALL, '')


def futureValueCalculator(mon_inv, yr_intr, num_yr):
    mon_rate = (yr_intr / 12) / 100
    total_mon = num_yr * 12
    futureValue = 0
    for i in range(0, total_mon):
        futureValue += mon_inv
        mon_intr = futureValue * mon_rate
        futureValue += mon_intr
    return futureValue
def dataInputs():
    while True:

        try:
            while True:
                monthlyInvestment = float(input('Enter Monthly investment:\t'))
                if monthlyInvestment > 0 and monthlyInvestment <= 100000:
                    monthlyInvestment = monthlyInvestment
                    break
                else:
                    print('Monthly investment must be more than 0')
            break

        except ValueError:
            print('Invalid entry')
            continue
    while True:
        try:
            while True:
                yearlyInterestRate = float(input('Enter yearly interest rate:\t'))
                if yearlyInterestRate > 0 and yearlyInterestRate <= 100:
                    yearlyInterestRate = yearlyInterestRate
                    break
                else:
                    print('Interest rate must be more than 0')
            break

        except ValueError:
            print('Invalid entry')
            continue
    while True:
        try:
            while True:
                numberOfYears = int(input('Enter number of years:\t'))
                if numberOfYears > 0 and numberOfYears <= 50:
                    numberOfYears = numberOfYears
                    break
                else:
                    print('Number of Years must be more than 0')
            break

        except ValueError:
            print('Invalid entry')
            continue


    return monthlyInvestment,yearlyInterestRate,numberOfYears




if __name__ == '__main__':
    loop = 'y'
    loop = loop.lower()
    while loop == "y":
        print('FUTURE VALUE PROGRAM'.center(100))
        print('Welcome to the Future Value Program'.center(100))
        print('='*100)
        print()
        monthlyInvestment, yearlyInterestRate, numberOfYears = dataInputs()

        futureValue = futureValueCalculator(monthlyInvestment, yearlyInterestRate, numberOfYears)
        print()
        print('{}: {:>10}'.format('Monthly investment',lc.currency(monthlyInvestment, grouping=True)))
        print('{}: {:>15.1f}'.format('Interest rate',yearlyInterestRate))
        print('{}: {:>23d}'.format('years',numberOfYears))
        print('{}: {:>16}'.format('Future Value',lc.currency(futureValue, grouping=True)))
        loop = input('Continue? (y/n): ')
        if loop == 'n':
            print('\nBye')
            break

