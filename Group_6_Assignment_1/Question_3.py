"""
Assignment 1

Question 3
"""

from Classes import Customer
import csv


def main():
    """
    Main code for program, calls other functions.
    """
    print("Customer Viewer")
    while True:
        
        cust_list = read()
        while True:
            try:                                         #Test variables:
                choice = int(input("\nEnter user ID: ")) #103 / 104 / 99
                break
            except ValueError:
                print("Invalid entry, try again.")
        
        state = check_id(choice, cust_list)
        
        print("\n" + f"{state}")
        
        cont = input("\nContinue? (y/n): ").lower()
        if cont == 'y':
            continue
        elif cont == 'n':
            break
        else:
            print("Invalid input, ending program.")
            break
    
    print("Bye!")


def read():
    """
    Converts each row in the csv file into a customer object and appends those objects to a list.

    Returns
    -------
    cust_info : list
        List of customer objects.
    """
    customer_info = []
    cust_info = []
    with open("customers.csv") as file:
        info = csv.reader(file)
        next(file)
        for row in info:
            customer_info.append(row)
    for customer in customer_info:
        cust = Customer(int(customer[0]), customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7])
        cust_info.append(cust)
    return cust_info


def check_id(choice, cust_list):
    """
    Checks the list of customers for one with a matching id to the user input.

    Parameters
    ----------
    choice : int
        User inputed id number.
    cust_list : list
        List of customer objects.

    Returns
    -------
    name : str
        Customer name and address info.
    """
    name = "No customer with that ID."
    
    for customer in cust_list:
        if customer.custid == choice:
            name = customer.custNameAddress()
        else:
            continue

    return name


if __name__ == "__main__":
    main()
