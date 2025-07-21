def shopping_cart():
    # 1. Predefined store items and prices
    store = {
        "apple": 3.0,
        "banana": 2.0,
        "milk": 6.5,
        "bread": 5.0,
        "eggs": 7.0
    }

    cart = []

    print("Welcome to the Shopping Cart Program!")

    while True:
        print("\nMenu:")
        print("1. View available items")
        print("2. Add item to cart")
        print("3. View cart and total price")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("\nAvailable items:")
            for item, price in store.items():
                print(f"- {item.title()}: {price} EGP")

        elif choice == "2":
            item = input("Enter the item name to add to cart: ").lower()
            if item in store:
                cart.append(item)
                print(f"{item.title()} has been added to your cart.")
            else:
                print(f"Sorry, '{item}' is not available in the store.")

        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                print("\nYour cart contains:")
                total = 0
                for item in cart:
                    print(f"- {item.title()}: {store[item]} EGP")
                    total += store[item]
                print(f"Total price: {total:.2f} EGP")

        elif choice == "4":
            print("Thank you for shopping! Goodbye.")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")

# Run the program
shopping_cart()

