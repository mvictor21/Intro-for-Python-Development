from re import X


clients = []

print("Enter a list of numbers, type 0 when finished.")

number = 0
while number != 0:
    new_client = input("What is the name of the new client? ")
    clients.append(new_client)

print()
print("The client list: ")

for client in clients:
    print(client)