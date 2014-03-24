import turtle
turtle.speed('fastest')

ANGLE = 60

def draw_levi(length, depth):
	if depth == 0:
		turtle.forward(length)
	else:
		draw_levi(length/3, depth-1)
		turtle.right(ANGLE)
		draw_levi(length/3, depth-1)
		turtle.left(2*ANGLE)
		draw_levi(length/3, depth-1)
		turtle.right(ANGLE)
		draw_levi(length/3, depth-1)
		

draw_levi(300, 4)
turtle.left(120)
draw_levi(300, 4)
turtle.left(120)
draw_levi(300, 4)
turtle.left(120)
input()