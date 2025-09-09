import turtle

sc = turtle.Screen()
#creating canvas
sc.bgcolor("red")

sc.setup(700, 700)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()
board.fillcolor("yellow")
board.begin_fill()
board.color("yellow")
board.pensize(100)

n = 10
# creating a square
for i in range(0,n):
    board.forward(75)
    board.right(360/n)

board.end_fill()
turtle.done()