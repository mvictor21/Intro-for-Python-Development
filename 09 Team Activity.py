clients = []

new_client = ""
while new_client != "end":
    new_client = input("What is the name of the new client? ")
    clients.append(new_client)

print()
print("The client list: ")

for client in clients:
    print(client)