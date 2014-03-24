import turtle
turtle.speed('fastest')
angle = 60
def draw_koh (length, n):
	if n == 0:
		turtle.forward(length)
	else:
		draw_koh(length / 3, n - 1)
		turtle.left(angle)
		draw_koh(length / 3, n - 1)
		turtle.right(angle * 2)
		draw_koh(length / 3, n - 1)
		turtle.left(angle)
		draw_koh(length / 3, n - 1)
draw_koh(300, 5)
input()
