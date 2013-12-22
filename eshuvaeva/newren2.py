import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1
length = 50
size = 50
for x in range(0, 15, 1):
	for y in range(0, 15, 1):
		c.create_rectangle( length + x * size , length + y * size, length + x * size - size,length +  y * size - size, fill = "saddle brown")

def location(event):
	c = event.widget 
	for x in range(0, 15, 1):
		for y in range(0, 15, 1):
			if event.x > (length + x * size)  and event.x < (length + (x + 1) * size) and event.y > (length + y * size)  and event.y < (length + (y + 1) * size):
				m = x
				n = y
	return(m,n)

def square(event):
	c = event.widget 
	location(event)
	if (event.x - (length + m * size)) > ((length + (m + 1) * size) - event.x):
		a = m + 1
	else:
		a = m

	if (event.y - (length + n * size)) > ((length + (n + 1) * size) - event.y):
		b = n + 1
	else:
		b = n
	return(a, b)
def white(event): 
	c = event.widget 
	square(event)
	c.create_oval( a - 0.5 ,b - 0.5 , a + 0.5, b + 0.5 , fill = 'white')
c.bind("<Button-1>", white) 
c.mainloop()
