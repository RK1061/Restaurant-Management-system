import json


with open("Restauran managment project/menu.json", "r") as f:
    data = json.load(f)

items = data.get('menu', [])

def main_menu():
    print('-' * 70)
    print(" W E L C O M E   T O   M A R A T H I   T A D A K A ".center(70))
    print('-' * 70)
    print("🛒 Order now and experience the taste of tradition!".center(70))
    print('-' * 70)
    print("1. Show Menu")
    print("2. Order Items")
    print("3. Update Menu")
    print("4. Exit")
    print('_' * 70)

    choice = int(input("Choose: "))
    return choice

# Main menu 
while True:
    choice = main_menu()

    # Option 1: Show Menu
    if choice == 1:
        print(" Filter By Category:")
        print("1. Main course")
        print("2. Roti")
        print("3. Desserts")
        print("4. Rice")
        print("5. All")
        print("6. Chinese")
        print("7. Starter")
        print('_' * 70)

        cat_choice = int(input("Choose category (1-7): "))
        cat_choice_map = {
            1: "main_course", 2: "roti", 3: "desserts",
            4: "rice", 5: "all", 6: "chinese", 7: "starter"
        }
        filter_menu = cat_choice_map.get(cat_choice)

        if filter_menu:
            print(" Veg Filter:")
            print("1. Veg only")
            print("2. Non-veg only")
            print("3. Both")
            customer_choice = int(input("Choose option (1-3): "))

            print(f" Showing menu for: {filter_menu.upper()}\n")
            print('_' * 70)

            # Prepare the list of items to display in a table-like format
            menu_data = []
            for item in items:
           
                category = item.get("category", "").lower().replace(" ", "_")
                if filter_menu == "all" or category == filter_menu:
                 
                    if customer_choice == 1 and item["veg"]:
                        menu_data.append([item["id"], item["name"], f"₹{item['price']}", "Veg"])
                    elif customer_choice == 2 and not item["veg"]:
                        menu_data.append([item["id"], item["name"], f"₹{item['price']}", "Non-Veg"])
                    elif customer_choice == 3:
                        veg_status = "Veg" if item["veg"] else "Non-Veg"
                        menu_data.append([item["id"], item["name"], f"₹{item['price']}", veg_status])

            if menu_data:
                # Printing table headers
                print(f"{'ID':<5}{'Item Name':<30}{'Price':<10}{'Type':<10}")
                print('-' * 55)
                
            
                for row in menu_data:
                    print(f"{row[0]:<5}{row[1]:<30}{row[2]:<10}{row[3]:<10}")
            else:
                print("No items found for the selected filter.")

        else:
            print("Invalid category choice.")

        again = input("Do you want to order now? (yes/no): ").strip().lower()
        if again == "yes":
            choice = 2
        else:
            print("Thank you! Visit again.")
            exit()

    # Option 2: Order Items by Name     
    elif choice == 2:
        print("Place your order")
        cart = []

        while True:
            order_input = input("Enter item name or keyword (or 'ok' to finish): ").strip().lower()
            if order_input == "ok":
                break

            matched_items = [item for item in items if order_input in item["name"].lower()]
            if not matched_items:
                print("No matching items found.")
                continue

            print("Matching items:")
            for i, item in enumerate(matched_items, start=1):
                veg_status = "Veg" if item["veg"] else "Non-Veg"
                print(f"{i}. {item['name']} - ₹{item['price']} -- {veg_status}")

            index_choice = int(input("Select item number to order: "))
            if index_choice < 1 or index_choice > len(matched_items):
                print("Invalid choice.")
                continue

            matched = matched_items[index_choice - 1]
            quantity = int(input(f"Enter quantity for {matched['name']}: "))

            cart.append({
                "name": matched["name"],
                "price": matched["price"],
                "quantity": quantity,
                "total": round(matched['price'] * quantity, 2)
            })
            print(f"{matched['name']} x {quantity} added to cart")

        if cart:
            print("Your order summary")
            print("_" * 70)
            grandtotal = 0
            for item in cart:
                print(f"{item['name']} x {item['quantity']} = ₹{item['total']}")
                grandtotal += item['total']
            print("_" * 70)
            print(f"Total amount: ₹{round(grandtotal, 2)}")
            print("_" * 70)
            if grandtotal > 1000:
                print("Congratulations! You qualify for a 10% discount on your order.")
                discount = grandtotal * 0.10
                finalamount = grandtotal - discount
                print("=" * 70)
                print(f"Bill Amount:{round(finalamount, 2)}")
                print("=" * 70)
            print("Thank you for your order!")
        else:
            print("No items ordered.")

    # Option 3: Update Menu
    elif choice == 3:
        print("Update Menu")
        print("1. Add Item")
        update_choice = int(input("Choose option (1-1): "))  # Only add item for now
        if update_choice == 1:
            item_name = input("Enter item name: ").strip()
            price = float(input("Enter item price: "))
            veg = input("Is item veg (yes/no): ").strip().lower() == "yes"
            category = input("Enter item category (main_course, roti, desserts, rice, all, chinese, starter): ").strip().lower().replace(" ", "_")
            items.append({
                "id": len(items) + 1,
                "name": item_name,
                "price": price,
                "category": category,
                "veg": veg,
            })
            print(f"{item_name} added to menu.")
            
            # Save the updated menu back to the JSON file
            with open("Restauran managment project/menu.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Menu updated successfully.")
            
            # Return to the main menu
            again = input("Do you want to update the menu? (yes/no): ").strip().lower()
            if again == "yes":
                continue  # Stay on update menu
            else:
                print("Dish added successfully. Returning to main menu.")
                continue  # Go back to the main menu

    # Option 4: Exit
    elif choice == 4:
        print("Thank you! Visit again.")
        break  # Exit the program

    else:
        print("Invalid choice, please try again.")
