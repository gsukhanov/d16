import turtle
turtle.speed('fastest')
def fractal_tree(steps, length, angle):
	if steps == 0:
		return 0
	turtle.forward(length)
	turtle.left(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.right(angle)
	turtle.right(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.left(angle)
	turtle.forward(-length)
def draw_minkovsky(steps, length):
	if steps < 1:
		turtle.forward(length)
		return 0
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
if int(input('1 or 2')) == 1:
	fractal_tree(10, 10, 10)
else:
	draw_minkovsky(4, 300)

import turtle
turtle.speed('fastest')
def fractal_tree(steps, length, angle):
	if steps == 0:
		return 0
	turtle.forward(length)
	turtle.left(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.right(angle)
	turtle.right(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.left(angle)
	turtle.forward(-length)
def draw_minkovsky(steps, length):
	if steps < 1:
		turtle.forward(length)
		return 0
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
if int(input('1 or 2')) == 1:
	fractal_tree(10, 10, 10)
else:
	draw_minkovsky(4, 300)

import turtle
turtle.speed('fastest')
def fractal_tree(steps, length, angle):
	if steps == 0:
		return 0
	turtle.forward(length)
	turtle.left(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.right(angle)
	turtle.right(angle)
	turtle.forward(length)
	fractal_tree(steps - 1, length, angle)
	turtle.forward(-length) 
	turtle.left(angle)
	turtle.forward(-length)
def draw_minkovsky(steps, length):
	if steps < 1:
		turtle.forward(length)
		return 0
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.left(90)
	draw_minkovsky(steps - 1, length / 4)
	turtle.right(90)
	draw_minkovsky(steps - 1, length / 4)
if int(input('1 or 2')) == 1:
	fractal_tree(10, 10, 10)
else:
	draw_minkovsky(4, 300)

