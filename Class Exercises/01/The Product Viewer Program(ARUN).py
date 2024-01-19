from pvpclass import Product

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start =1):
        print(f"{i}. {product.name}")
    print()

def show_ind_product(product):
    width = 18
    print(f"{'Name:':{width}} {product.name}")
    print(f"{'Price:':{width}} {product.price:.2f}")
    print(f"{'Discount Percent:':{width}} {product.discount_percent:d}%")
    print(f"{'Discount Rate:': {width}} {product.getDiscountamount():.2f}")
    print(f"{'Discount Price:': {width}} {product.getDiscountprice():.2f}")
    print()

def get_products():
    return (Product("Stanley 13oz Wood Hammer", 12.99, 62),
            Product("Nation Hardware 3/4' Wire Nails", 2.00, 0),
            Product("Economy Duct Tape, 60yds, Silver", 5.99, 2))

def get_individual_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number <1 or number > len(products):
                print("Invalid Product.")
            else:
                return products[number-1]
        except ValueError:
            print("Invalid Number. Please Try Again.")
            print()

def main():
    print("THE PRODUCT VIEWER PROGRAM\n")
    products = get_products()
    show_products(products)

    choice = 'y'
    while choice.lower() == 'y':
        product = get_individual_product(products)
        show_products(product)

        choice = input("View Another Product? (y/n): ").lower()
        print()

    print("Bye!")

if __name__ == "__main__":
    main()




