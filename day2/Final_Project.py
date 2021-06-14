print("Welcome to the tip calculator.")
bill = input("What was the total bill?\nRs")
bill = float(bill)
tip = input(f"What percentage tip would you like to give?, 10, 12 , or 15? ")
tip = int(tip)
people = input("How many people to split the bill? ")
people = int(people)


x = float(bill + bill * (tip/100))
x /= people


print(f"Each person should pay: Rs", x)