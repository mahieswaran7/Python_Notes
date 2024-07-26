def add_function(menu_card, add_item):
    menu_card.append(add_item)
    return menu_card

def update_function(menu_card, update_list, update_item):
    if update_list < len(menu_card):
        menu_card[update_list] = update_item
    else:
        print(f"Index {update_list} is out of range.")

    return menu_card

def delete_function(menu_card, remove_item):
    if remove_item in menu_card:
        menu_card.remove(remove_item)
    else:
        print(f"{remove_item} not found in menu.")

    return menu_card

def main():
    menu_card = ["Paneer Naan", "Corn with pepper", "Veg salad", "French fries", "Cheesy burger"]
    
    while True:
        choice = input("\nEnter your choice from 1 to 4 (or 'q' to quit): ")

        if choice == '1':
            print("\nMenu Card:")
            print(menu_card)
        elif choice == '2':
            add_list = input("Enter the starter food you want to add: ")
            menu_card = add_function(menu_card, add_list)
            print("\nUpdated Menu Card:")
            print(menu_card)
        elif choice == '3':
            update_index = int(input("Enter the index to update (0 to {}): ".format(len(menu_card) - 1)))
            update_item = input("Enter the new item: ")
            menu_card = update_function(menu_card, update_index, update_item)
            print("\nUpdated Menu Card:")
            print(menu_card)
        elif choice == '4':
            remove_item = input("Enter the item to remove: ")
            menu_card = delete_function(menu_card, remove_item)
            print("\nUpdated Menu Card:")
            print(menu_card)
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number (1 to 4) or 'q' to quit.")

if __name__ == "__main__":
    main()
