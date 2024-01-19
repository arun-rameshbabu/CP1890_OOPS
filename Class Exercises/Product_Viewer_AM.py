# Importing product class
from Classes_ex import Product

def products_list():
    """
    This function creates a list of products.
    :return product1, product2, product3 (list):
    """
    product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
    product2 = Product("National Hardware 3/4\" Wire Nails", 2.00, 4)
    product3 = Product("Economy Duct tape, 60 yards, Silver", 6.99, 15)

    return [product1, product2, product3]

def user_input():
    """
    This function accepts and returns an input from the user.
    :return user (int):
    """
    while True:
        try:
            user = int(input("Enter product number: "))
            if user < 1 or user > len(products_list()):
                print("Invalid Input")
            else:
                return user
        except ValueError:
            print("Invalid Input, please try again")

def select_product(choice):
    """
    This function uses the user input to select a product
    :param choice (int):
    :return product:
    """
    product = "NONE"
    prod1, prod2, prod3 = products_list()
    while product == "NONE":
        if choice == 1:
            product = prod1
        elif choice == 2:
            product = prod2
        elif choice == 3:
            product = prod3
        else:
            print("Invalid Selection, Please try again.\n")
    return product

def product_viewer(product):
    """
    This function displays information about the chosen product
    :param product:
    """
    print(f"\nProduct Name:\t\t {product.name}")
    print(f"Product Price:\t\t {product.price:.2f}")
    print(f"Discount Percent:\t {product.discountPercent:d}%")

    print(f"Discount Amount:\t {product.get_discountAmount():.2f}")
    print(f"Discount Price:\t\t {product.get_discountPrice():.2f}")

def continue_value():
    """
    This function accepts and returns a user input
    :return contin (str):
    """
    contin = input("\nView another product? (y/n): ").lower()
    while contin != "y" and contin != "n":
        contin = input("\nUnknown command, try again:\nView another product? (y/n): ").lower()
    return contin

def main():
    """
    Main function for the program, calls all other functions
    """
    print("The Products Viewer program\n")
    prod1, prod2, prod3 = products_list()

    print("PRODUCTS")
    print(f"1.{prod1.name}")
    print(f"2.{prod2.name}")
    print(f"3.{prod3.name}\n")

    cont = True
    while cont == True:
        choice = user_input()
        product = select_product(choice)
        product_viewer(product)
        cont_val = continue_value()
        if cont_val == "n":
            cont = False

if __name__ == "__main__":
    main()
    print("Goodbye!")
