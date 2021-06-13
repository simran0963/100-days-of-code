import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names) - 1
random_name = random.randint(0 , x)
bill_person = names[random_name]
print(f"The bill is under", bill_person)

random.choice(names)