import Sales_Inheritance_Classes as sic


def menu():
    """
    Prints Command Menu
    """
    print("\nCOMMAND MENU\nview - View all sales\nadd - Add Sales")
    print("menu - Show menu\nexit - Exit program")
    return


def day_input(month):
    """
    Parameters
    ----------
    month : Int
        Month of sale.

    Returns
    -------
    day : Int
        Day of sale.
    """
    if month == 4 or month == 6 or month == 9 or month == 11:
        day = int(input("Day(1-30):\t\t"))
        if day < 1 or day > 30:
            print("Day should be 1-30.\n")
            day = day_input(month)
    elif month == 2:
        day = int(input("Day(1-28):\t\t"))
        if day < 1 or day > 28:
            print("Day should be 1-28.\n")
            day = day_input(month)
    else:
        day = int(input("Day(1-31):\t\t"))
        if day < 1 or day > 31:
            print("Day should be 1-31.\n")
            day = day_input(month)
    return day


def view(data, sales):
    """
    Parameters
    ----------
    data : INT
        Number 0 for list purposes.
    sales : List or False
        List of sales.
    """
    total = 0
    num = 0
    if sales == False:
        print("No sales to view.\n")
    else:
        print("\t\t\tDate\t\t\tQuarter\t\t\tAmount")
        print('-' * 60)
        for data in sales:
            num += 1
            print(f"\n{num}.\t\t\t{data[0]}-{data[1]}-{data[2]}\t\t{quarter(data[1])}\t\t\t\t${float(data[3])}")
            total = float(total) + float(data[3])
        print('-' * 60)
        print(f"TOTAL:\t\t\t\t\t\t\t\t\t\t${total}")


def add(data, sales):
    """
    Parameters
    ----------
    data : INT
        Number 0 for list purposes.
    sales : List or False
        List of sales.
    """
    if sales == False:
        sales = []
    amount = float(input("Amount:\t\t\t"))
    while amount <= 0:
        print("Sales amount must be greater than zero.")
        amount = float(input("\nAmount:\t\t\t"))
    year = int(input("Year:\t\t\t"))
    while year < 1900 or year > 3000:
        print("Year must bebetween 1900 and 3000.\n")
        year = int(input("Year (1900-3000):\t\t\t"))
    month = int(input("Month (1-12):\t"))
    while month < 1 or month > 12:
        print("Month must be between 1 and 12.\n")
        month = int(input("Month (1-12):\t"))
    day = day_input(month)
    data += 1
    sales.append([data, year, month, day, amount])
    print(f"Sales data for {year}-{month}-{day} has been added.")


def import_data(sales):
    prior_data = sic.read_txt()
    new_data = input("Enter name of file to import: ")
    if new_data in prior_data:
        print(f"File '{new_data}' has already been imported.")
    else:
        import_data = sic.read_list(new_data)
        for data in import_data:
            sales.append(import_data)
        sic.write_txt("sales_log.txt", new_data)


def quarter(month):
    """
    Parameters
    ----------
    month : INT
        Month of sale.

    Returns
    -------
    quarter : INT
        Quarter of sale.

    """
    if month >= 1 and month < 4:
        quarter = 1
    elif month >= 4 and month < 7:
        quarter = 2
    elif month >= 7 and month < 10:
        quarter = 3
    elif month >= 10 and month < 13:
        quarter = 4
    return quarter


def logic(data, sales):
    """
    Parameters
    ----------
    data : INT
        Number 0 for list purposes.
    sales : List or False
        List of sales.
    """
    cmd = input("\nPlease enter a command: ")

    cont = 'x'
    while cont == 'x':
        if cmd.lower() == "view":
            view(data, sales)
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "add":
            add(data, sales)
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "import":
            import_data(sales)
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "menu":
            menu()
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "exit":
            cont = 'a'
        else:
            print("Invalid Command. Please try again.")
            menu()
            cmd = input("\nPlease enter a command: ")
    return


def main():
    """
    Calls all functions.
    """
    print("SALES DATA IMPORTER\n")

    sales = sic.read_list("all_sales.csv")

    data = 0
    menu()
    logic(data, sales)
    sic.write_list(sales)
    print("\nBye!")


if __name__ == "__main__":
    main()
