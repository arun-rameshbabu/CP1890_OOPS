"""
Assignment 1

Question 3
"""

from csv_class import Customer
import csv


def main():
    while True:
        print("Customer Viewer\n")
        
        cust_list = read()
                                               #Test variables:
        choice = int(input("Enter user ID: ")) #103 / 104 / 99
        
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
    name = "No customer with that ID."
    
    for customer in cust_list:
        if customer.custid == choice:
            name = customer.custNameAddress()
        else:
            continue

    return name


if __name__ == "__main__":
    main()
