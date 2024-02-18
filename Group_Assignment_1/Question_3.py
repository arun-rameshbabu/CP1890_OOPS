"""
Assignment 1

Question 3
"""

from csv_class import Customer
import csv


def main():
    print("Customer Viewer\n")
    
    cust_list = read()
    
    choice = int(input("Enter user ID: "))
    
    for customer in cust_list:
        if customer.id == choice:
            customer.custNameAddress()



def read():
    customer_info = []
    cust_info = []
    with open("customers.csv") as file:
        info = csv.reader(file)
        next(file)
        for row in info:
            customer_info.append(row)
    for customer in customer_info:
        cust = Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7])
        cust_info.append(cust)
    return cust_info


if __name__ == "__main__":
    main()
