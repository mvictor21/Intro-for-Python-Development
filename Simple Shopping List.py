cart_items = []

new_item = ""
while new_item != "quit":
    new_item = input("Please enter the items of the shopping list (type: 'quit' to finish): ")
    cart_items.append(new_item)

print()
print("The shopping list is: ")

for items in cart_items:
    print(f"Item: {items}")

for items in cart_items:
    print(items)

for i in range(len(cart_items)):
    print(f"{i}. {items}")