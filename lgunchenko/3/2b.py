import tkinter
def turn(): 
	c.delete(*c.find_all())
	y = 15
	pl = 0
	while pl < n - 1:
		if F[pl] < F[pl + 1]:
			F[pl] = 1
			F[pl + 1] = 0
			pl += 1
		pl += 1
	x = 10
	for draw in range(n):
		if F[draw] == 0:
			c.create_line(x + 25 * draw, y, x + 20 + 25 * draw, y)
			c.create_line(x + 20 + 25 * draw, y, x + 15 + 25 * draw, y - 5)
			c.create_line(x + 20 + 25 * draw, y, x + 15 + 25 * draw, y + 5)
		if F[draw] == 1:
			c.create_line(x + 25 * draw , y, x + 20 + 25 * draw, y)
			c.create_line(x + 25 * draw, y, x + 5 + 25 * draw, y - 5)
			c.create_line(x + 25 * draw, y, x + 5 + 25 * draw, y + 5)
	if F != B:
		c.after(100, turn)
	c.create_text(50,100, text = "You\nwin!")
c = tkinter.Canvas(width = 1000, height = 600)
c.pack() 
n = int(input())
F = []
for i in range(n):
	F.append(int(input()))
B = []
for x in F:
    B.append(x)
for i in range(n - 1):
	for j in range(n - 1):
		if B[j] < B[j + 1]:
			B[j] = 1
		B[j + 1] = 0
turn()
c.mainloop()