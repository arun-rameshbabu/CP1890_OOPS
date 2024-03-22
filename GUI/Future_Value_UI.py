import locale as lc
import tkinter as tk
from tkinter import ttk

def future_value(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest

    lc.setlocale(lc.LC_ALL, 'en_US')

    future_value_calc = lc.currency(future_value, grouping=True)
    return future_value_calc

def main():
    Calculator = tk.Tk()
    Calculator.title('Future Value Calculator')
    Calculator.geometry('500x500')

    Window = ttk.Frame(Calculator, padding='10 10 10 10')
    Window.pack(fill = 'both', expand = True)
    monthly_investment_label = ttk.Label(Window, text ='Enter monthly investment:\t\t')
    monthly_investment_label.grid(row = 0, column =0)
    monthly_investment = tk.IntVar(value=0)
    monthly_investment_entry = ttk.Entry(Window,width=40,textvariable = monthly_investment)
    monthly_investment_entry.grid(row = 0, column = 1)

    yearly_interest_label = ttk.Label(Window, text ='Enter yearly interest:\t\t')
    yearly_interest_label.grid(row =1, column = 0)
    yearly_interest = tk.IntVar(value=0)
    yearly_interest_entry = ttk.Entry(Window,width=40,textvariable =yearly_interest)
    yearly_interest_entry.grid(row = 1, column =1)
    years_label = ttk.Label(Window, text ='Enter number of years:\t\t ')
    years_label.grid(row =3,column = 0)
    years = tk.IntVar(value=0)
    years_entry = ttk.Entry(Window, width=40,textvariable =years)
    years_entry.grid(row = 3, column =1)

    future_value_calc = future_value(monthly_investment_entry.get(), yearly_interest_entry.get(), years_entry.get())
    monthly_investment = lc.currency(monthly_investment_entry, grouping=True)

    print(f"{'Monthly investment:':20} {monthly_investment:>10}")
    print(f"{'Interest Rate:':20} {yearly_interest:>10.2f}")
    print(f"{'Years:':20} {years:>10}")
    print(f"{'Future Value:':20} {future_value_calc:>10}")

    choice = input('Continue? (y/n): ').lower()
    print()

if __name__ == '__main__':
    main()