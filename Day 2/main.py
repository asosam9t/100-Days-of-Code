#This code is for a software that calculates the total bill to be paid including the tip.

#print greeting
print("Hello, Welcome to the tip calculator")

#The questions to be asked

Bill = input("Please enter your total bill\n$")
Tip = input("How much tip will you like to give in percentage? e.g 10\n")
Persons = input("How many people are to split the bill?\n")

# The logic

logic1 = (int(Bill) + (int(Tip) / 100))
logic2 = round((logic1 / int(Persons)), 2)
logic3 = "{:.2f}".format(logic2)

#Output result
print(f"Each person should pay: ${logic3}")
