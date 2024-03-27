import tkinter as tk
from tkinter import ttk, messagebox


def future_value(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest
    return future_value


def clicked_calc_button():
    monthly_investment = monthly_value.get()
    yearly_interest_rate = yearly_value.get()
    years = num_years_value.get()
    if monthly_investment == '' or yearly_interest_rate == '' or years == '':
        messagebox.showerror('Value Error', 'Some entries were left blank')
    else:
        future_v = future_value(float(monthly_investment), float(yearly_interest_rate), int(years))
        fv_text.set(f"${future_v:.2f}")


def exit_button_clicked():
    fv_window.destroy()


fv_window = tk.Tk()
fv_window.title("Future Value Calculator")
fv_window.geometry("400x300")

frame = ttk.Frame(fv_window, padding='10 10 10 10')
frame.pack(fill='both', expand=True)

# Monthly investment label
monthly_label = ttk.Label(frame, text="Monthly Investment:")
monthly_label.grid(row=0, column=0, sticky=tk.E)

# Monthly investment entry box
monthly_value = tk.StringVar()
monthly_entry = ttk.Entry(frame, width=25, textvariable=monthly_value)
monthly_entry.grid(column=1, row=0, columnspan=2)

# Yearly interest label
yearly_label = ttk.Label(frame, text="Yearly Interest Rate:")
yearly_label.grid(column=0, row=1, sticky=tk.E)

# Yearly interest entry box
yearly_value = tk.StringVar()
yearly_entry = ttk.Entry(frame, width=25, textvariable=yearly_value)
yearly_entry.grid(column=1, row=1, columnspan=2)

# Number of years label
num_years_label = ttk.Label(frame, text="Years:")
num_years_label.grid(column=0, row=2, sticky=tk.E)

# Number of years entry box
num_years_value = tk.StringVar()
num_years_entry = ttk.Entry(frame, width=25, textvariable=num_years_value)
num_years_entry.grid(column=1, row=2, columnspan=2)

# Future value label
fv_label = ttk.Label(frame, text="Future Value:")
fv_label.grid(column=0, row=3, sticky=tk.E)

# Future value output
fv_text = tk.StringVar()
fv_entry = ttk.Entry(frame, width=25, textvariable=fv_text, state='readonly')
fv_entry.grid(column=1, row=3, columnspan=2)

# Buttons 1 and 2
calc_button = ttk.Button(frame, text="Calculate", command=clicked_calc_button)
calc_button.grid(column=1, row=4)
exit_button = ttk.Button(frame, text="Exit", command=exit_button_clicked)
exit_button.grid(column=2, row=4)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

fv_window.mainloop()
