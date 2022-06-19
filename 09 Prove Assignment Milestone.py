cart_items = []
cart_total = 0
item_price = 0

print("Welcome to the Shopping Cart Program!")
print("Please, enter an action:")
while cart_items != 5:
    new_item = input("What item would you like to add? ")
    cart_items.append(new_item)
    print(f"{new_item} has been added to the cart.")

def addItem(item_name, item_price):
    print(cart_items[0])
cart_total += item_price

cartsummary = {}
cartsummary = dict((item, cart_items.count(item))for item in cart_items)

for i in range(0, len(cart_items)):
    print(cart_items[i])