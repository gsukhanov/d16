import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1

length = 25
size = 50
for x in range(1, 16, 1):
	for y in range(1, 16, 1):
		c.create_rectangle( length + x * size , length + y * size, length + x * size - size,length +  y * size - size, fill = "saddle brown")
def location(event, a , b):
	global x
	global y
	if event.x > (length + x * size)  and event.x < (length + (x + 1) * size) and event.y > (length + y * size)  and event.y < (length + (y + 1) * 50):
		a = x 
		b = y
def white(event): 
	c = event.widget 
	for k in range(1, 15, 1):
		for z in range(1, 15, 1):
			location(k, z)
			c.create_oval( k , z , k + 1, z + 1, fill = "white")
c.bind("<Button-1>", white) 
 
c.mainloop()
