import tkinter
def draw(): 
	c.delete(*c.find_all())
	s=25
	y = 15
	k = 0
	l = 0
	while k < n - 1:
		if a[k] < a[k + 1]:
			a[k] = 1
			a[k + 1] = 0
			k += 1
			l += 1
		k += 1
	x = 10
	for i in range(n):
		if a[i] == 0:
			c.create_text (x + s * i, y, text="——>")
		if a[i] == 1:
			c.create_text (x + s * i, y, text="<——")
	if l > 0:
		c.after(1000, draw)
	else:
		c.create_text(50,100, text="You win! Play again!")
		return
c = tkinter.Canvas(width=1000, height=1000)
c.pack()
n = int(input())
a = []
for i in range(n):
	a.append(int(input()))
draw()
c.mainloop()