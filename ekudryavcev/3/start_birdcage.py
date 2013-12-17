import tkinter
from collections import namedtuple

Bridge = namedtuple("Bridge", ["xpos", "ypos", "player", "direction"])
dirct = 0

print("Input the size of the cage in dots width; from 6 to 15")
size = 8
if size < 6 or size > 15:
	print("Wrong size, restart the game")
c = tkinter.Canvas(width = 100 + 50 * size, height = 100 + 50 * size)
c.pack()

def cancrea(c):
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

def bridgeit(b , c):
	if b.direction=="hor":
		c.create_line(b.xpos , b.ypos , b.xpos + 50 , b.ypos , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos + 50 , b.ypos , fill = b.player , width = 3)
	else:
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 50 , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 50 , fill = b.player , width = 3)

def click(event):
	global playermove
	global dirct
	c = event.widget
	xp = event.x - 25
	yp = event.y - 50
	nex = xp // 25
	ney = yp // 25
	print(nex, ney)
	sumx = nex + ney
	sumy = nex - ney + 2
	if int((sumx + sumy)) % 4 == 0 and int((sumx - sumy)) % 4 == 0:
		if playermove == "red":
			dirct = "vert"
			nex += - 1
			ney += 1
		if playermove == "blue":
			dirct = "hor"
	if int((sumx + sumy)) % 4 == 2 and int((sumx - sumy)) % 4 == 2:
		if playermove == "blue":
			dirct = "vert"
		if playermove == "red":
			dirct = "hor"
	b = Bridge(nex * 25 + 25 , ney * 25 + 50 , playermove , dirct)
	bridges.append(b)
	bridgeit(b , c)
	#print(xp , yp , nex , ney , b.xpos , b.ypos)
	if playermove == "red":
		playermove = "blue"
	else:
		playermove = "red"

cancrea(c)

playermove = "red"
c.bind("<Button-1>", click)

bridges = []

c.mainloop()