import turtle
turtle.speed('fastest')

ANGLE = 45

def draw_levi(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        turtle.right(ANGLE)
        draw_levi(length/(2**0.5), depth-1)
        turtle.left(2*ANGLE)
        draw_levi(length/(2**0.5), depth-1)
        turtle.right(ANGLE)

draw_levi(300, 10)
input()
