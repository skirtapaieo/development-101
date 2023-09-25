# define the classs and initialize the variables
class Inventory:
    def __init__(self, max_capacity): # constructor
        self.max_capacity = max_capacity # max capacity of the inventory
        self.inventory = [] # empty list
        self.total_quantity = 0 # total quantity of items in the inventory

    # add item to the inventory
    def add_item(self, name, price, quantity):
        if self.total_quantity + quantity > self.max_capacity:
            print("Inventory is full!")
            return False
        for item in self.inventory:
            if item["name"] == name: # if item already exists in the inventory
                print("Item already exists!")
                return False
        self.inventory.append({"name": name, "price": price, "quantity": quantity}) # add item to the inventory
        self.total_quantity += quantity # update total quantity
        return True

    # remove item from the inventory
    def delete_item(self,name):
        for item in self.inventory: # iterate through the inventory
            if item["name"] == name: # if item exists in the inventory
                self.total_quantity -= item["quantity"] #
                self.inventory.remove(item) #
                return True # return True if item is removed
        return False # if item does not exist in the inventory

    # get most stocked item
    def get_most_stocked_item(self):
        if not self.inventory:
            return None # if inventory is empty
        most_stocked_item = max(self.inventory, key=lambda item: item["quantity"]) # get item with maximum quantity
        return most_stocked_item["name"] # return name of the most stocked item

    def get_items_in_price_range(self, min_price, max_price):
        #
        items_in_range = [item['name'] for item in self.inventory if min_price <= item['price'] <= max_price]
        return items_in_range
