from pvpclass import Product

product1 = Product("Stanley 13oz Wood Hammer",12.99, 62)
product2 = Product('National Hardware 3/4" Nails', 12.99, 62)
product3 = Product("Economy Duct Tape", 12.99, 62)
def title():
    print("The Product Viewer Program\n")
    print("Products")
    for i, product in enumerate([product1.name, product2.name, product3.name],start=0):

        print(i, product)


def main():
    title()
    program = True
    while True:
        choice = int(input("\nEnter Product Number:  "))
        if choice == 1:
            print(f"Product Name:\t\t {product1.name}")
            print(f"Product Price:\t\t {product1.price:.2f}")
            print(f"Discount Percent:\t {product1.discountPercent:d}%")

            print(f"Discount Amount:\t {product1.getDiscountamount():.2f}")
            print(f"Discount Price:\t\t {product1.getDiscountprice():.2f}")
            choice2 = input("\nView Another Product (y/n)?")
            if choice2.lower == 'n':
                break

if __name__ == "__main__":
    main()