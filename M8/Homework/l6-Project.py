import turtle

turtle.Screen().bgcolor("light blue")
board = turtle.Turtle()
board.pensize(2)
board.color("dark blue")
board.fillcolor("yellow")
board.begin_fill()

for _ in range(6):
    board.forward(100)
    board.left(60)

board.end_fill()
turtle.done()