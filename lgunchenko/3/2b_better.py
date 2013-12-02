import tkinter
def turn(): 
	c.delete(*c.find_all())
	y = 15
	pl = 0
	ch = 0
	while pl < n - 1:
		if F[pl] < F[pl + 1]:
			F[pl] = 1
			F[pl + 1] = 0
			pl += 1
			ch += 1
		pl += 1
	x = 10
	for draw in range(n):
		if F[draw] == 0:
			c.create_text (x + 25 * draw, y, text = "-->")
		if F[draw] == 1:
			c.create_text (x + 25 * draw, y, text = "<--")
	if ch > 0:
		c.after(1000, turn)
	else:
		c.create_text(50,100, text = "You win!")
		return
c = tkinter.Canvas(width = 1000, height = 600)
c.pack() 
n = int(input())
F = []
for i in range(n):
	F.append(int(input()))
turn()
c.mainloop()