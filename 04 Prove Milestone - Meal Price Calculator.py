from unicodedata import decimal


print("Please enter the following information:")
print()
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_number = input("What is the number of childrens? ")
adult_number = input("What is the number of adults? ")
tax_rate = float(input("What is the sales tax rate? "))

total_child_meal = float(child_meal) * int(child_number)
total_adult_meal = float(adult_meal) * int(adult_number)
sub_total = (total_child_meal + total_adult_meal)
sales_tax = float(sub_total) * int(tax_rate) / 100
total_amount = (sub_total + sales_tax)
print()
print(f"What's the price of a child's meal? ${child_meal}")
print(f"What's the price of an adult's meal? ${adult_meal}")
print(f"How many children are there? {child_number}")
print(f"How many adults are there? {adult_number}")
print(f"What is the sales tax rate? {tax_rate}%")
print()
print(f"Subtotal: ${sub_total}")
print(f"Sales Tax: ${sales_tax}")
print(f"Total: ${total_amount}")
print()
payment_amount = float(input("What is the payment amount? "))
change = (payment_amount - total_amount)
chng=round(change, 2)
print(f"Change: $"+str (chng) + "")