import tkinter
c = tkinter.Canvas(width = 1000, height = 600)
c.pack() 
n = int(input())
a = []
def turn(): 
	c.delete(*c.find_all())
	y = 15
	x = 0
	t = 0
	while x < n - 1:
		if a[x] < a[x + 1]:
			a[x] = 1
			a[x + 1] = 0
			x += 1
			t += 1
		x += 1
	x = 10
	for draw in range(n):
		if a[draw] == 0:
			c.create_text (x + 25 * draw, y, text = "-->")
		if a[draw] == 1:
			c.create_text (x + 25 * draw, y, text = "<--")
	if t > 0:
		c.after(1000, turn)
	else:
		c.create_text(50,100, text = "You win!")
		return
for i in range(n):
	a.append(int(input()))
turn()
c.mainloop()