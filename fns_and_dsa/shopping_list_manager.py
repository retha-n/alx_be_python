'''shopping_list = []
def add_item(item):

def removing_item(item):

def display_items(iteem)'''

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input("Enter the item to add: "))

        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter Item you would like to remove: ")
            for i in shopping_list:
                if shopping_list[i] != remove_item:
                    print('item not found')
                else:
                    shopping_list.remove(remove_item)
            
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
