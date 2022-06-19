cart_items = []

print("Welcome to the Shopping Cart Program!")
print()

def menu():

        print("1. Add a new item")
        print("2. Display the content of the shopping cart")
        print("3. Quit")

def display_content():
    print(cart_items[0])
for i in range(0, len(cart_items)):
        print(cart_items[i])

menu()
option = int(input("Please, enter an action: "))

while option != 3:
    if option == 1:
        new_item = input("What item would you like to add? ")
        print(f"{new_item} has been added to the cart.")
        cart_items.append(new_item)
    elif option == 2:
        print("The content of the shopping cart are:")
        cartsummary = {}
        cartsummary = dict((item, cart_items.count(item))for item in cart_items)
        for i in range(0, len(cart_items)):
            print(cart_items[i])
    else:
        print("Invalid option, please, try again.")

    print()
    menu()
    option = int(input("Please, enter an action: "))

print("Thank you for using the shopping cart program. Good bye!")