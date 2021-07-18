import random
from art import scissors, rock, paper
import os

def clear():
	os.system('cls')

clear()
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if choose > 3 or choose < 0 :
	print("You chose an invalid number, you lose.")
if choose == 0 :
	print("your choice:")
	print(rock)
	

	choice =random.randint(0, 3)



	if choice == 0 :
		print(rock)
		print("The match is a draw, play again.")
	elif choice == 1 :
		print(paper)
		print("You lose.")
	else :
		print(scissors)
		print("You win!")
if choose == 1 :
	print("your choice:")
	print(paper)
	choice =random.randint(0, 2)



	print("Computer chooses:")
	if choice == 0 :
		print(rock)
		print("You win!")
	elif choice == 1 :
		print(paper)
		print("The match is a draw, play again.")
	else :
		print(scissors)
		print("You lose.")



if choose == 2 :
	print("your choice:")
	print(scissors)
	choice =random.randint(0, 3)

	print("Computer chooses:")
	if choice == 0 :
		print(rock)
		print("You lose.")
	elif choice == 1 :
		print(paper)
		print("You win!")
	else :
		print(scissors)
		print("The match is a draw, play again.")
