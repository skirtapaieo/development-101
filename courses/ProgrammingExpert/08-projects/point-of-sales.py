import asyncio


class Inventory:
    def __init__(self):
        self.catalogue = {
            "Burgers": {
                "1": {"name": "Python Burger", "price": 5.99},
                "2": {"name": "C Burger", "price": 4.99},
                "3": {"name": "Ruby Burger", "price": 6.49},
                "4": {"name": "Go Burger", "price": 5.99},
                "5": {"name": "C++ Burger", "price": 7.99},
                "6": {"name": "Java Burger", "price": 7.99},
            },
            "Sides": {
                "7": {"name": "Small Fries", "price": 2.49},
                "8": {"name": "Medium Fries", "price": 3.49},
                "9": {"name": "Large Fries", "price": 4.29},
                "10": {"name": "Small Caesar Salad", "price": 3.49},
                "11": {"name": "Large Caesar Salad", "price": 4.49},
            },
            "Drinks": {
                "12": {"name": "Small Coke", "price": 1.99},
                "13": {"name": "Medium Coke", "price": 2.49},
                "14": {"name": "Large Coke", "price": 2.99},
                "15": {"name": "Small Ginger Ale", "price": 1.99},
                "16": {"name": "Medium Ginger Ale", "price": 2.49},
                "17": {"name": "Large Ginger Ale", "price": 2.99},
                "18": {"name": "Small Chocolate Milk Shake", "price": 3.99},
                "19": {"name": "Medium Chocolate Milk Shake", "price": 4.49},
                "20": {"name": "Large Chocolate Milk Shake", "price": 4.99},
            },
        }

        self.stock = {
            "1": 10,
            "2": 10,
            "3": 10,
            "4": 10,
            "5": 10,
            "6": 10,
            "7": 10,
            "8": 10,
            "9": 10,
            "10": 10,
            "11": 10,
            "12": 10,
            "13": 10,
            "14": 10,
            "15": 10,
            "16": 10,
            "17": 10,
            "18": 10,
            "19": 10,
            "20": 10,
        }

    async def get_number_of_items(self):
        return len(self.catalogue)

    async def get_catalogue(self):
        return self.catalogue

    async def get_stock(self, item_id):
        return self.stock.get(item_id, 0)

    async def decrement_stock(self, item_id):
        if item_id in self.stock:
            self.stock[item_id] -= 1

    async def get_item(self, item_id):
        return self.catalogue.get(item_id)


async def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


async def display_catalogue(catalogue):
    print("--------- Burgers -----------\n")
    for item_id, item in catalogue["Burgers"].items():
        print(f"{item_id}. {item['name']} ${item['price']:.2f}")
    print("\n---------- Sides ------------\n")
    for category, items in catalogue.items():
        if category != "Burgers" and category != "Drinks":
            for item_id, item in items.items():
                print(f"{item_id}. {item['name']} ${item['price']:.2f}")
    print("\n---------- Drinks ------------\n")
    for item_id, item in catalogue["Drinks"].items():
        print(f"{item_id}. {item['name']} ${item['price']:.2f}")
    print("\n------------------------------\n")


async def create_order(inventory):
    order = []
    catalogue = await inventory.get_catalogue()
    await display_catalogue(catalogue)
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")

    while True:
        item_id = await get_user_input("Enter an item number: ")

        if item_id == "q":
            break

        item = await inventory.get_item(str(item_id))

        if item is None:
            print("Please enter a valid number.")
            continue

        stock = await inventory.get_stock(str(item_id))
        if stock <= 0:
            print("Sorry, this item is out of stock.")
            continue

        order.append(item)
        await inventory.decrement_stock(str(item_id))

    return order


async def create_combos(order):
    combos = []
    combo = {"items": [], "price": 0}
    for item in order:
        if len(combo["items"]) < 3:
            combo["items"].append(item)
            combo["price"] += item["price"]
        else:
            combos.append(combo)
            combo = {"items": [item], "price": item["price"]}

    if combo["items"]:
        combos.append(combo)

    return combos


async def calculate_order_total(order, combos):
    subtotal = sum(item["price"] for item in order)
    combo_prices = sum(combo["price"] * 0.85 for combo in combos)
    tax = (subtotal + combo_prices) * 0.05
    total = subtotal + combo_prices + tax

    return subtotal, tax, total


async def confirm_order(total):
    while True:
        choice = input(f"Would you like to purchase this order for ${total:.2f} (yes/no)? ").lower()
        if choice == "yes":
            print("Thank you for your order!")
            return True
        elif choice == "no":
            print("No problem, please come again!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


async def place_order(inventory):
    order = await create_order(inventory)
    combos = await create_combos(order)

    print("\nHere is a summary of your order:\n")
    for combo in combos:
        print(f"${combo['price']:.2f} Burger Combo")
        for item in combo["items"]:
            print(f"  {item['name']}")
    for item in order:
        if item not in [item for combo in combos for item in combo["items"]]:
            print(f"${item['price']:.2f} {item['name']}")

    subtotal, tax, total = await calculate_order_total(order, combos)

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    if await confirm_order(total):
        return True
    else:
        return False


async def main():
    inventory = Inventory()
    print("Welcome to the ProgrammingExpert Burger Bar!")
    print("Loading catalogue...")
    await asyncio.sleep(1)
    await place_order(inventory)

    while True:
        choice = input("Would you like to make another order (yes/no)? ").lower()
        if choice == "yes":
            await place_order(inventory)
        elif choice == "no":
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    asyncio.run(main())
