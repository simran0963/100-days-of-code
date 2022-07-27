from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
	tim.right(10)
def move_left():
	tim.left(10)
def move_backward():
	tim.backward(10)
def move_forward():
	tim.forward(10)
def clearscr():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="D", fun=move_right)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="C",fun=clearscr)
screen.exitonclick()