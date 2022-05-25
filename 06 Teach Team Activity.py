can_ride = False

print("Please enter the following information:")
print()
age_one = int(input("What is the age of the firts rider? "))
height_one = int(input("What is the height of the first rider? "))

second_rider = input("Is there a second rider yes/no? ")

if second_rider.lower() == "yes":
    age_two = int(input("What is the age of the second rider? "))
    height_two = int(input("What is the height of the second rider? "))

    if height_one >= 18 or height_two >= 18:
        can_ride = True
    else:
        if age_one < 18 or age_two < 18:
                can_ride = False
        else:
            can_ride = False
else:
    if age_one >= 18 and height_one >= 62:
        can_ride = True
    else:
        can_ride = False
if can_ride:
    print("Welcome to the marathon!")
else:
    print("Sorry, you can't run this marathon")