from turtle import Turtle
import random
tim = Turtle()

colours = ["CornflowerBlue", "tomato", "dark goldenrod", "deep pink", "dark violet", "DarkOrchid","IndianRed", "DeepSkyBlue","LightSeaGreen","SlateGray","SeaGreen", "green yellow", "wheat", "light sky blue", "light blue", "navajo white", "violet"]
def draw_shape(sides):
	angle = 360 / sides
	for _ in range(sides):
		tim.forward(100)
		tim.right(angle)

for shape in range(3,50):
	tim.color(random.choice(colours))
	tim.pensize(3)
	draw_shape(shape)

# for size in range(3,11):
# 	for _ in range(sides):
# 		tim.forward(100)
# 		tim.right(angle)
# 	sides+=1
# 	angle = 360/sides
# my_screen = Screen()
# my_screen.exitonclick()