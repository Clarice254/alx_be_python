def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Starts with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':  # Add item to the list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':  # Remove item from the list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == '3':  # View the list
            if len(shopping_list) > 0:
                print("\nYour Shopping List contains the following items:")
                index = 0
                while index < len(shopping_list):
                    print(f"{index + 1}. {shopping_list[index]}")
                    index += 1
            else:
                print("There are no items in your shopping list at the moment.")
        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:  # Invalid input handling
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
