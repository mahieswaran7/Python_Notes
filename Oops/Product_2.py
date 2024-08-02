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

def find_product(product_id, product_list):
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

def add_product_from_input(product_list):
    print("Enter product details:")
    name = input("Product Name: ")
    try:
        price = float(input("Price: "))
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        return

    description = input("Description: ")
    
    # Create and add the product to the list
    new_product = Product(name, price, description)
    new_product.add_product(product_list)
    print(f"Product '{name}' added successfully with ID {new_product.product_id}.")

def list_all_products(product_list):
    # List all products with their details
    if not product_list:
        print("No products available.")
        return
    print("\nList of all products:")
    for product in product_list:
        print(f"ID: {product.product_id}, Name: {product.product_name}, Price: ${product.price:.2f}, Description: {product.product_description}")

def interactive_product_search(product_list):
    while True:
        # Prompt the user for a product ID or to quit
        user_input = input("Enter a product ID to search or type 'quit' to exit: ")
        
        if user_input.lower() == 'quit':
            print("Exiting the search.")
            break

        # Try to convert the user input to an integer
        try:
            product_id = int(user_input)
            details = find_product(product_id, product_list)
            print(details)
        except ValueError:
            print("Invalid input. Please enter a valid product ID or 'quit' to exit.")

# List to store all product instances
product_list = []

# Example usage
print("Welcome to the Product Management System")
while True:
    print("\nChoose an option:")
    print("1. Add a new product")
    print("2. Search for a product by ID")
    print("3. List all products")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_product_from_input(product_list)
    elif choice == '2':
        interactive_product_search(product_list)
    elif choice == '3':
        list_all_products(product_list)
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

