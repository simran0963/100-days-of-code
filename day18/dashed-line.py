from turtle import Turtle, Screen
tim = Turtle()
for _ in range(15):
	tim.pendown()
	tim.forward(10)
	tim.penup()
	tim.forward(10)

my_screen = Screen()
my_screen.exitonclick()