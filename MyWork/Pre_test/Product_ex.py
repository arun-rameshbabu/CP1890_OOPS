from Classes_ex import Product

# Creating the Products
product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Marker", 2.00, 4)

print("Product Data\n" + "-"*35)
print(f"Product Name:\t\t {product1.name}")
print(f"Product Price:\t\t {product1.price:.2f}")
print(f"Discount Percent:\t {product1.discountPercent:d}%")

print(f"Discount Amount:\t {product1.get_discountAmount():.2f}")
print(f"Discount Price:\t\t {product1.get_discountPrice():.2f}")
