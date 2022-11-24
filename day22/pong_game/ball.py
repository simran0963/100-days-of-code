from turtle import Turtle

class Ball(Turtle):
	def __init__(self):
		ball = Turtle()
		super().__init__()
		self.color("white")
		self.shape("circle")
		self.penup()

	def move(self):
		new_x = self.xcor() + 10
		new_y = self.ycor() + 10