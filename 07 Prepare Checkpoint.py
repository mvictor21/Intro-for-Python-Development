positive_number = int(input("Please, type a positive number: "))

while positive_number < 0:
    print("Sorry, that is a negative number: ")
    positive_number = int(input("Please, type a possitive number: "))

print(f"the number is {positive_number}")