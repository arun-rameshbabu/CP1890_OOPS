import csv

#Creating Customer Class
class Customer:
    def __init__(self, cust_id, first_name, last_name, company_name, address, city, state, zip):
        self.cust_id = cust_id
        self.firstName = first_name
        self.lastName = last_name
        self.company = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zip
#Creating Property that returns full name from CSV
    @property
    def full_name(self):
        return f"{self.firstName} {self.lastName}"
#Creating Propert that returns Full Address; extra line if company included
    @property
    def full_address(self):
        if self.company:
            return f"{self.company}\n{self.address}\n{self.city}, {self.state} {self.zipcode}"
        else:
            return f"{self.address}\n{self.city}, {self.state} {self.zipcode}"

#Creating function that reads customer data from CSV file and puts it into a list.
def read_customer_data(file_path):
    customers = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer = Customer(
                row['cust_id'],
                row['first_name'],
                row['last_name'],
                row['company_name'],
                row['address'],
                row['city'],
                row['state'],
                row['zip']
            )
            customers.append(customer)
    return customers

#Creating function that will display customers by ID
def display_customer_by_id(customers, cust_id):
    for customer in customers:
        if customer.cust_id == cust_id:
            print(f"{customer.full_name}")
            print(f"{customer.full_address}\n")
            return
    print(f"No customer with ID: {cust_id}.")

#Main function that calls Customer class
def main():
    file_path = 'customers.csv'
    choice = 'y'
    while choice == 'y':
        #Headline
        print("Customer Viewer\n")

        # Read customer data from CSV file
        customers_list = read_customer_data(file_path)
        # Get user input for customer ID
        customer_id_input = input("Enter Customer ID: ")
        print()
        # Display customer information
        display_customer_by_id(customers_list, customer_id_input)
        #Continue program input
        choice = input("Continue (y/n)?:  \n")


if __name__ == "__main__":
    main()


