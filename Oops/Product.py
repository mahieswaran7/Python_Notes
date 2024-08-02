class Product:
    # Static variable to keep track of the next product ID
    next_id = 1

    def __init__(self, name, price, description):
        self.product_id = Product.next_id
        Product.next_id += 1
        self.product_name = name
        self.price = price
        self.product_description = description

    def add_product(self, product_list):
        # Add this product instance to the product_list
        product_list.append(self)
        return self

    def get_product_details(product_id, product_list):
        # Iterate through the product_list to find the product with the matching ID
        for product in product_list:
            if product.product_id == product_id:
                return {
                    "Product ID": product.product_id,
                    "Product Name": product.product_name,
                    "Price": product.price,
                    "Description": product.product_description
                }
        return "Product not found."

# List to store all product instances
product_list = []

# Example usage
# Creating and adding products
product1 = Product("Laptop", 1200.99, "A high-performance laptop.")
product1.add_product(product_list)

product2 = Product("Phone", 799.49, "A smartphone with a great camera.")
product2.add_product(product_list)

# Retrieving product details
# Note: Using instance method for retrieval in this example
def find_product(product_id, product_list):
    for product in product_list:
        if product.product_id == product_id:
            return {
                "Product ID": product.product_id,
                "Product Name": product.product_name,
                "Price": product.price,
                "Description": product.product_description
            }
    return "Product not found."

print(find_product(1, product_list))  # Should return details of the product with ID 1
#print(find_product(3, product_list))  # Should return "Product not found." because ID 3 does not exist
