age = input("What is your current age?\n")
age = int(age)

days = (365 * 90) - (365 * age)
weeks = (52 * 90) - (52 * age)
months = (12 * 90) - (12 * age)
result = f"You have {days} days, {weeks} weeks, and {months} months left."
print(result)