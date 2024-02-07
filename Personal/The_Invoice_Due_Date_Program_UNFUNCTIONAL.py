from datetime import datetime


def invoice_date():
    invoice = input("Enter the invoice date (MM/DD/YY): ")
    return datetime.strptime(invoice, "%m/%d/%y")


def main():
    print("The Invoice Due Date Program")

    invoice_date()
    due_date = datetime.strptime("2021, 13, 2", "%y/%d/%m")
    time_left = due_date - datetime.now()

    if time_left >= due_date:
        print(f"this invoice is {time_left} days(s) overdue")


if __name__ == "__main__":
    main()
