from Classes_Constructor import Product

# creating the products
product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Marker", 2.00, 4)

print("Product Data")
print(f"Product Name: \t\t\t{product1.name}")
print(f"Product Price: \t\t\t{product1.price}")
print(f"Discount Percent: \t\t{product1.discount_percent}:0%")

print(f"Discount Amount: \t\t{product1.getDiscountAmount():.2f}")
print(f"Discount Price: \t\t{product1.getDiscountPrice():.2f}")