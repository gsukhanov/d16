import tkinter
from collections import namedtuple

Bridge = namedtuple("Bridge", ["xpos", "ypos", "player", "direction"])
dirct = 0

print("Input the size of the cage in dots width; from 6 to 15. Then input cell size")
cell = 30
size = 8
if size < 6 or size > 15:
	print("Wrong size, restart the game")
c = tkinter.Canvas(width = 60 + (2 * cell * size), height = 60 + (2 * cell * size) )
c.pack()

def cancrea(c): #canvas created
	x = cell
	y = 2 * cell
	for i in range (size + 1):
		x = 3 * cell
		for i2 in range (size):
			c.create_oval(x + cell - 2, y - 2, x + cell + 2, y + 2, fill = "blue")
			x += 2 * cell
		y += 2 * cell

	x = 2 * cell
	y = cell
	for i in range (size + 1):
		y = 3 * cell
		for i2 in range (size):
			c.create_oval(x + cell - 2, y - 2, x + cell + 2, y + 2, fill = "red")
			y += 2 * cell
		x += 2 * cell

def bridgeit(b , c): #drawing a bridge
	if b.direction=="hor":
		c.create_line(b.xpos , b.ypos , b.xpos + 2 * cell , b.ypos , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos + 2 * cell , b.ypos , fill = b.player , width = 3)
	else:
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 2 * cell , fill = "black" , width = 5)
		c.create_line(b.xpos , b.ypos , b.xpos , b.ypos + 2 * cell , fill = b.player , width = 3)

def click(event): #creating new bridge information
	global playermove
	global dirct
	c = event.widget
	nex = (event.x - cell) // (2 * cell)
	ney = (event.y - 2 * cell) // (2 * cell)
	print(nex, ney)
	sumx = nex + ney
	sumy = nex - ney
	if (sumx + sumy) % 2 == 0:
		if playermove == "red":
			dirct = "hor"
			nex = nex * 2
			ney = ney * 2 + 2
		if playermove == "blue":
			dirct = "vert"
			nex = nex * 2 + 1
			ney = ney * 2 + 1
	else:
		if playermove == "blue":
			dirct = "hor"
			nex = nex * 2 + 1
			ney = ney * 2 + 1
		if playermove == "red":
			dirct = "vert"
			ney = ney * 2 + 2
	#bridge direction and its vertices found and saved
	b = Bridge(nex * cell + cell , ney * cell + cell , playermove , dirct)
	bridgeit(b , c)
	if playermove == "red": #this changes the player
		red_bridges.append(b)
		playermove = "blue"
	else:
		blue_bridges.append(b)
		playermove = "red"

cancrea(c)

playermove = "red"
c.bind("<Button-1>", click) #finally a bridge drawed

red_bridges = []
blue_bridges = []

c.mainloop()