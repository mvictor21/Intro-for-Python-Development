print("Please enter the following information:")
print()
child_meal = int(input("What's the price of a child's meal? "))
adult_meal = int(input("What's the price of an adult's meal? "))
child_number = input=("What's the number of childrens? ")
adult_number = input=("What's the number of adults? ")
tax_rate = float(input("What's the sales tax rate'? "))

total_child_meal = int(child_meal) * int(child_number)
total_adult_meal = int(adult_meal) * int(adult_number)
sub_total = int(total_child_meal) + int(total_adult_meal)
sales_tax = float(sub_total) * float(tax_rate) / 100
total_amount = float(sub_total) + float(sales_tax)
print()
print(f"What's the price of a child's meal? {child_meal}")
print(f"What's the price of an adult's meal? {adult_meal}")
print(f"How many children are there? {child_number}")
print(f"How many adults are there? {adult_number}")
print(f"What is the sales tax rate? {tax_rate}")
print()
print(f"Subtotal: {sub_total}")
print(f"Sales Tax: {sales_tax}")
print(f"Total: {total_amount}")
print()
payment_amount = float(input("What is the payment amount? "))
change = float(payment_amount) - float(total_amount)
print(f"Change: {change}")





# Ask The user:
# The price of a child's meal (floating point)
# The price of an adult's meal (floating point)
# The number of children (integer)
# The number of adults (integer)
# The sales tax rate (floating point)

# Then, complete the following steps:
# Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal,
# and multiplying the number of adults by the price of their meal and adding those two values together.
# Display the subtotal.
# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
# Compute and display the total price of the meal by adding the subtotal and the sales tax.

#Finally:
# Ask the user for the the payment amount (floating point)
# Compute and display the change.

#Final Result:
#What is the price of a child's meal? 4.50
#What is the price of an adult's meal? 9.00
#How many children are there? 4
#How many adults are there? 2
#What is the sales tax rate? 6

#Subtotal: $36.00
#Sales Tax: $2.16
#Total: $38.16

#What is the payment amount? 40
#Change: $1.84

# Showing Creativity and Exceeding Requirements
# For this assignment, you could add anything else to the meal, such as drinks,
# appetizers, or a tip percentage, or anything else you can think of. Play around
# with different ideas and see what you can learn!

# ** Milestone Requirements **
# At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:
# Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
# Ask the user for the number of adults and children and store these values properly into variables as integers.
# Ask the user for the sales tax rate and store the value properly as a floating point number.
# Compute and display the subtotal (don't worry about rounding to two decimals at this point).

# Final requirements
# At the end of Lesson 04, in addition to the milestone requirements above, you need to also complete the following:
# Compute and display the sales tax.
# Compute and display the total.
# Ask the user for the payment amount and store the value properly as a floating point number.
# Compute and display the change.
# Include a dollar sign ($) before each displayed value.
# Display each value to two decimals.
# Double check that the calculations are correct.
# Show creativity and exceed the core requirements by adding additional features.
# Use good style in your program, including variable names and whitespace.