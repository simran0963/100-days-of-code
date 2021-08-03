import os

def clear():
	os.system('cls')

clear()

#import a random module to select either heads or tails
import random

random_integer = random.randint(0, 1)
print(random_integer)

if random_integer == 0 :
	print("Heads")

elif random_integer == 1 :
	print("Tails")