# ==========================================
# Product Information System (Real-Time Use)
# Example: Flipkart / Online Shopping App
# ==========================================

# Taking unique Product ID (used as primary key in databases)
product_id = int(input("Enter Product ID: "))

# Taking Product Name displayed on the website
product_name = input("Enter Product Name: ")

# Taking product price entered by the seller
price = float(input("Enter Price: "))

# Taking product categories for filtering (Electronics, Wearable, etc.)
categories_input = input("Enter Categories (comma-separated): ")

# Converting categories into a list
categories = [cat.strip() for cat in categories_input.split(",")]

# Taking available stock in warehouse
available_stock = int(input("Enter Available Stock: "))

# Taking number of products already sold
sold_stock = int(input("Enter Sold Stock: "))

# Storing stock details in a tuple (fixed record)
stock_details = (available_stock, sold_stock)

# Taking discount percentage for offers or sales
discount_percentage = float(input("Enter Discount Percentage: "))

# Taking product features shown on product page
features_input = input("Enter Product Features (comma-separated): ")

# Converting features into a set to remove duplicates
product_features = set(feature.strip() for feature in features_input.split(","))

# Taking supplier name (used for inventory management)
supplier_name = input("Enter Supplier Name: ")

# Taking supplier contact number
supplier_contact = input("Enter Supplier Contact Number: ")

# Taking supplier location
supplier_location = input("Enter Supplier Location: ")

# Storing supplier details in dictionary (key-value format)
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# ==========================================
# Displaying Output Using Formatting Methods
# ==========================================

print("\n========= PRODUCT DETAILS =========\n")

# 1. Using Comma Separation (used in logs & reports)
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Product Discount: %.2f%%" % discount_percentage)

# 3. Using f-strings (used in dashboards & UI)
print(f"\nProduct Name: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")

# 4. Using .format() method (used in invoices & summaries)
print(
    "\nSupplier Details: Name - {}, Contact - {}, Location - {}".format(
        supplier_details["name"],
        supplier_details["contact"],
        supplier_details["location"]
    )
)

# Displaying remaining data