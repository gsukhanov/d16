import tkinter
x = int(input())
y = int(input())
m = int(input())
c = tkinter.Canvas(width = 1000,height = 1000)
c.pack()
def draw_star(canvas, x, y, m):
	x1 = x + m
	x2 = x + 2*m
	x3 = x + m/2
	x4 = x1 + m/2
	y1 = y - m/2
	y2 = y
	y3 = y + m
	y4 = y3
	canvas.create_line(x, y, x2, y2)
	canvas.create_line(x, y, x4, y4)
	canvas.create_line(x3, y3, x2, y2)
	canvas.create_line(x1, y1, x3, y3)
	canvas.create_line(x1, y1, x4, y4)

draw_star(c, x, y, m)	


c.mainloop()