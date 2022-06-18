friends = []

name = ""

while name != "end":
    name = input("Type the name of a friend: ")
    friends.append(name)

print()
print("Your friends are:")

for friend in friends:
    print(friend)