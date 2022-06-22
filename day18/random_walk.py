from turtle import Screen
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	random_colour =  (r, g, b)
	return random_colour

turns = [0, 90, 270, 180]
tim.pensize(5)
tim.speed("fastest")
for _ in range(500):
	tim.color(random_color())
	tim.forward(10)
	tim.setheading(random.choice(turns))
		
my_screen = Screen()
my_screen.exitonclick()