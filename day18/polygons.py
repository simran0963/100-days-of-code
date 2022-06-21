from turtle import Turtle
import random
tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid","IndianRed", "DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen", "green yellow", "wheat", "light sky blue", "light blue", "navajo white", "violet"]
def draw_shape(sides):
	angle = 360 / sides
	for _ in range(sides):
		tim.forward(100)
		tim.right(angle)

for shape in range(3,10):
	tim.color(random.choice(colours))
	draw_shape(shape)

# for size in range(3,11):
# 	for _ in range(sides):
# 		tim.forward(100)
# 		tim.right(angle)
# 	sides+=1
# 	angle = 360/sides
# my_screen = Screen()
# my_screen.exitonclick()