from class1 import Customer
import csv

file_path = "customers.csv"

def title():
    print("Customer Viewer")



def read_customers_from_csv(csv_file):
    customers = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = Customer(
                cust_id=int(row['cust_id']),
                first_name=row['first_name'],
                last_name=row['last_name'],
                company_name=row['company_name'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                zip=row['zip']
            )
            customers.append(customer)
    return customers


def display_customer_by_id(customers, customer_id):
    for customer in customers:
        if customer.cust_id == customer_id:
            print()
            print(customer.full_name)
            print(customer.full_address)
            return
    print("No customer with that ID.")


def main():
    title()
    customers = read_customers_from_csv("customers.csv")
    while True:
        try:
            customer_id = int(input("\nEnter customer ID: "))
            display_customer_by_id(customers, customer_id)
        except ValueError:
            print("Invalid Customer ID.")
        again = input("\nDo you want to continue? (y/n): ")
        if again == "y":
            continue
        else:
            break
    print("\nBye!")



if __name__ == "__main__":
    main()