from datetime import datetime, date, time, timedelta

print("The Invoice Due Date program\n")

while True:
    invoice = input("Enter the invoice date (MM/DD/YYYY): ")  # 1/14/2024
    invoice_date = datetime.strptime(invoice, "%m/%d/%Y")
    due = "2/13/2024"
    due_date = datetime.strptime(due, "%m/%d/%Y")
    days = (datetime.now() - due_date)
    print()

    print(f"Invoice Date: {invoice_date:%B %d, %Y}")
    print(f"Due Date: {due_date:%B %d, %Y}")
    print(f"Current Date: {date.today():%B %d, %Y}")

    print(f"\nThis invoice is {timedelta(days.days)}(s) overdue.")

    cont = input("\nContinue? (y/n): ").lower()
    if cont == 'n':
        break
    elif cont != 'y':
        print("Invalid entry, Ending Program.")
        break
print('Goodbye!')
