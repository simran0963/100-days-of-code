from turtle import Turtle, Screen
import random

is_race_on = False
scr = Screen()
scr.setup(width=500,height=400)
user_bet = scr.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-125,-75,-25,25,75,125]
turtles = []

for turt_ind in range(0,6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colours[turt_ind])
	new_turtle.penup()
	new_turtle.goto(x=-230,y=y_pos[turt_ind])
	turtles.append(new_turtle)
	
if user_bet:
	is_race_on = True

while is_race_on:
	for turt in turtles:
		if turt.xcor() > 230:
			is_race_on = False
			winning_turt = turt.pencolor()
			if winning_turt == user_bet:
				print(f"You won! The {winning_turt} is the winner!")
			else:
				print(f"You've lost. The {winning_turt} is the winner.")

		rand_dis = random.randint(0,10)
		turt.forward(rand_dis)

scr.exitonclick()