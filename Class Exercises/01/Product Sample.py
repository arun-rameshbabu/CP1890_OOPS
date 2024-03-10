from classes import Product
import locale as lc
lc.setlocale(lc.LC_ALL, 'EN-ca')

product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Marker", 2.00, 4)

print("Product Data")
print(f"Product Name:\t\t {product1.name}")
print(f"Product Price:\t\t {product1.price:.2f}")
print(f"Discount Percent:\t {product1.discountPercent:d}%")

print(f"Discount Amount:\t {product1.getDiscountamount():.2f}")
print(f"Discount Price:\t\t {product1.getDiscountprice():.2f}")