# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_categories():
    """Display available categories from the 'products' dictionary."""
    print("Available categories:")
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")


def display_products(products_list):
    """Display the products from the selected category."""
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price}")


def display_sorted_products(products_list, sort_order):
    # Sort products list based on price
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])  # Sort by price in ascending order
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)  # Sort by price in descending order



def add_to_cart(cart, product, quantity):
    # Unpack product name and price from product tuple
    product_name, product_price = product
    # Append product to cart as a tuple (product_name, product_price, quantity)
    cart.append((product_name, product_price, quantity))



def display_cart(cart):
    total_cost = 0
    for item in cart:
        product_name, product_price, quantity = item
        item_total = product_price * quantity
        total_cost += item_total
        print(f"{product_name} - ${product_price} x {quantity} = ${item_total}")
    print(f"Total cost: ${total_cost}")



def generate_receipt(name, email, cart, total_cost, address):
    """Generate and display the receipt with the shopping details."""
    print(f"Receipt for {name} ({email}):")
    for product, quantity in cart:
        print(f"{product}: {quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery to: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")


def validate_name(name):
    """Validate that the name has two parts and contains only alphabets."""
    parts = name.split()
    if len(parts) == 2 and all(part.isalpha() for part in parts):
        return True
    return False


def validate_email(email):
    """Validate the email address contains the '@' symbol."""
    return "@" in email


def main():
    """Main function that drives the shopping experience."""
    # Get user's name and validate
    name = input("Enter your full name: ")
    while not validate_name(name):
        print("Invalid name. Please enter both first and last name with only alphabets.")
        name = input("Enter your full name: ")

    # Get user's email and validate
    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []
    total_cost = 0

    while True:
        # Display categories
        display_categories()
        try:
            category_choice = int(input("Select a category by number: "))
            if category_choice < 1 or category_choice > len(products):
                print("Invalid choice. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Get the selected category and display products
        category = list(products.keys())[category_choice - 1]
        print(f"\nProducts in {category}:")
        product_list = products[category]
        display_products(product_list)

        # Product selection or sorting
        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to categories")
            print("4. Finish shopping")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                try:
                    product_choice = int(input("Select a product by number: "))
                    if product_choice < 1 or product_choice > len(product_list):
                        print("Invalid product number. Please try again.")
                        continue
                    quantity = int(input("Enter quantity: "))
                    product, price = product_list[product_choice - 1]
                    add_to_cart(cart, product, quantity)
                    total_cost += price * quantity
                    print(f"Added {quantity} x {product} to cart.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue

            elif choice == "2":
                try:
                    sort_order = int(input("Sort by price: 1 for ascending, 2 for descending: "))
                    if sort_order not in [1, 2]:
                        print("Invalid sort order. Please try again.")
                        continue
                    sorted_list = display_sorted_products(product_list, sort_order)
                    display_products(sorted_list)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

            elif choice == "3":
                break

            elif choice == "4":
                if cart:
                    display_cart(cart)
                    print(f"Total cost: ${total_cost}")
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                return

            else:
                print("Invalid choice. Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()
