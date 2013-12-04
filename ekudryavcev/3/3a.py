import tkinter
print("Input the size of the cage in dots width; from 6 to 15")
siz = int(input())
if siz < 6 or siz > 15:
	print("Wrong size, restart the game")
else:
	c = tkinter.Canvas(width = 100 + 50 * siz, height = 100 + 50 * siz)
	c.pack()

x = 50
y= 50
for i in range (siz + 1):
	x = 50
	for i2 in range (siz):
		c.create_oval(x + 23, y - 2, x + 27, y + 2, fill = "blue")
		x += 50
	y += 50

x = 25
y= 75
for i in range (siz + 1):
	y = 75
	for i2 in range (siz):
		c.create_oval(x + 23, y - 2, x + 27, y + 2, fill = "red")
		y += 50
	x += 50

c.mainloop()