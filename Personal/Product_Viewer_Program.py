def title():
    product1 = product("stanley 13 ounce Wood Hammer")
    product2 = product('National Hardware 3/4" Wire Nails')
    product3 = product('Economy Duct Tape, 60 yds, silver')

    print("The Product Viewer Program\n")
    print("PRODUCTS")
    print(f"1. {product1}")
    print(f"2. {product2}")
    print(f"3. {product3}")

def main():
    title()

if __name__ == "__main__":
    main()