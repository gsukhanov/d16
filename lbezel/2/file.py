import tkinter
c = tkinter.Canvas(width = 1000, height = 1000)
a = int(input())
b = int(input())
c.pack()
def k_t(canvas, x, y, x1, y1):
	x = 500 + x
	y = 500 - y
	x1 = x1 + 500
	y1 = 500 - y1
	c.create_line(x, y, x1, y1)
c.create_line(0, 500, 1000, 500)
c.create_line(500, 0, 500, 1000)
def f_x(x):
	y = (x - a)*(x - a)/m
	return y
x = -500
m = 50
for u in range(1000):	
	y = f_x(x) + b
	x1 = x + 1
	y1 = f_x(x1) + b
	
	
	k_t(c, x, y, x1, y1)
	x = x1
c.mainloop()