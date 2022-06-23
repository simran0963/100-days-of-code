# import colorgram
import random
import turtle as t
from turtle import Screen
tim = t.Turtle()
t.colormode(255)

color_list  = [(233, 233, 236), (233, 232, 228), (236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]
tim.penup()
tim.backward(500)
tim.left(90)
tim.forward(300)
tim.right(90)
for _ in range(10):
	for _ in range(10):
		tim.speed("fastest")
		tim.dot(20, random.choice(color_list))
		# tim.penup()
		tim.forward(50)
	tim.right(90)
	# tim.penup()
	tim.forward(50)
	tim.right(90)
	tim.forward(500)
	tim.left(180)
	
my_screen = Screen()
my_screen.exitonclick()
# rgb_colors = []
# colors = colorgram.extract('C:\\Users\\HP\\OneDrive\\Documents\\REPOSITORIES\\100-days-with-code\\day18\\Hirst Painting\\image.jpg', 30)
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g	
# 	b = color.rgb.b
# 	new_color = (r, g, b)
# 	rgb_colors.append(new_color)
