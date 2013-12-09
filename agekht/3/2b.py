print ("Hello!")
import tkinter

def draw(): 
	c.delete(*c.find_all())
	x = 15
	rt = 0
	cl = 0
	while rt < n - 1:
		if array [rt] < array [rt + 1]:
			array [rt] = 1
			array [rt + 1] = 0
			rt += 1
			cl += 1
		rt += 1
	y = 10
	for i in range (n):
		if array [i] == 0:
			c.create_text (y + 25 * i, x, text="=>")
		if array [i] == 1:
			c.create_text (y + 25 * i, x, text="<=")
	if cl > 0:
		c.after (1000, draw)
	else:
		c.create_text (60, 120, text="Perfect! Maybe another game?")
		return
		
c = tkinter.Canvas (width = 1000, height = 800)
c.pack () 
n = int(input())
array = []
for i in range (n):
	array.append(int(input()))
draw()
c.mainloop()