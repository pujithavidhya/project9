# Tuple-Based Product Catalogue Audit

# Create product catalogue using tuples
products = (
    ("Laptop", 55000, 10),
    ("Mobile", 20000, 15),
    ("Tablet", 15000, 8),
    ("Headphones", 2000, 20)
)

# Display product catalogue
print("Product Catalogue:")
for product in products:
    print(product)

# Find total inventory value
total = 0

for product in products:
    price = product[1]
    quantity = product[2]
    total = total + (price * quantity)

print("\nTotal Inventory Value:", total)

# Find the most expensive product
highest = products[0]

for product in products:
    if product[1] > highest[1]:
        highest = product

print("\nMost Expensive Product:", highest[0])
print("Price:", highest[1])

# Find products with low stock
print("\nProducts with Low Stock:")

for product in products:
    if product[2] < 10:
        print(product[0])