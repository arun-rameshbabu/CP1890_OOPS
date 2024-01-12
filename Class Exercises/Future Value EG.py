import locale as lc
lc.setlocale(lc.LC_ALL, 'EN-ca')
run = True
while True:
    month_i = int(input('Enter monthly investment:  '))
    year_i = float(input('Enter yearly interest rate:  '))
    years = int(input('Enter number of years:  '))



    print(f'\nMonthly investment: {lc.currency(month_i)}')
    print(f'Interest Rate: {year_i}')
    print(f'Years: {years}')
    future_value = 0
    for i in range(years*12):
        future_value += month_i
        mont_interest = future_value * ((year_i/12)/100)
        future_value += mont_interest
    print(f"Future Value: {lc.currency(future_value)}")
    cont = input("\nContinue? (y/n)")
    if cont.lower() == 'n':
        print('Bye!')
        break


