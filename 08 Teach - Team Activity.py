#print("This is line one", end="")
#print("This is line two")

word = "commitment"

favourite_letter = input("What is your favourite letter? ")

for letter in word:

    if letter.lower() == favourite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")

print()