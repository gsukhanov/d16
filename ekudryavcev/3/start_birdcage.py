import tkinter
from collections import namedtuple

Bridge = namedtuple("Bridge", ["xpos", "ypos", "player", "direction"])

print("Input the size of the cage in dots width; from 6 to 15")
size = int(input())
if size < 6 or size > 15:
	print("Wrong size, restart the game")
c = tkinter.Canvas(width = 100 + 50 * size, height = 100 + 50 * size)
c.pack()

def neau(c):
	x = 50
	y= 50
	for i in range (size + 1):
		x = 50
		for i2 in range (size):
			c.create_oval(x + 23, y - 2, x + 27, y + 2, fill = "blue")
			x += 50
		y += 50

	x = 25
	y= 75
	for i in range (size + 1):
		y = 75
		for i2 in range (size):
			c.create_oval(x + 23, y - 2, x + 27, y + 2, fill = "red")
			y += 50
		x += 50

neau(c)

def bridgeit(b , c):
	if b.direction=="hor":
		c.create_line(b.xpos , b.ypos , b.xpos + 50 , b.ypos , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos + 50 , b.ypos , fill = b.player , width = 3)
	else:
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 50 , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 50 , fill = b.player , width = 3)

def click(event):
	c = event.widget
	xp = event.x
	yp = event.y
	b = Bridge(xp , yp , "blue" , "vert")
	bridges.append(b)
	bridgeit(b , c)

c.bind("<Button-1>", click)

bridges = []


c.mainloop()