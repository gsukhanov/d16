import tkinter
def change(): 
	c.delete(*c.find_all())
	y = 15
	pl = 0
	ch = 0
	while pl < n - 1:
		if A[pl] < A[pl + 1]:
			A[pl] = 1
			A[pl + 1] = 0
			pl += 1
			ch += 1
		pl += 1
	x = 10
	for i in range(n):
		if A[i] == 0:
			c.create_text (x + 25 * i, y, text = "-->")
		if A[i] == 1:
			c.create_text (x + 25 * i, y, text = "<--")
	if ch > 0:
		c.after(1000, change)
	else:
		c.create_text(50,100, text = "You win!")
		return
c = tkinter.Canvas(width = 1000, height = 600)
c.pack() 
n = int(input())
A = []
for i in range(n):
	A.append(int(input()))
change()
c.mainloop()