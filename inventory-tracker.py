inventory = []

def display_menu():
    print("\nInventory Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display inventory")
    print("4. Total inventory value")
    print("5. Exit")

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity : "))
    price = float(input("Enter price: "))
    inventory.append((item_name, quantity, price))
    print(f"Item {item_name} added to inventory.")

def remove_item():
    item_name = input("Enter item name to remove: ")
    global inventory
    inventory = [item for item in inventory if item[0] != item_name]
    print(f"Item {item_name} removed from inventory.")

def total_inventory_value():
    total_value = sum(item[1] * item[2] for item in inventory)
    print(f"Total inventory value: ₹{total_value:.2f}")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    sorted_inventory = sorted(inventory, key=lambda x: x[0])
    print("\nInventory List:")
    for item in sorted_inventory:
        print(f"Item: {item[0]}, Quantity: {item[1]} , Price: ₹{item[2]:.2f}")
    
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            total_inventory_value()
        elif choice == "5":
            print("Exiting inventory system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
