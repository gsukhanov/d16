import tkinter
i = int(input())
j = int(input())
c = tkinter. Canvas (width=500, height=500)
c.pack()
def draw_cell (k, l):
	if k % 2 == l % 2:
		c.create_rectangle (50 * k, 50 * l, 50 * (k + 1), 50 * (l + 1), fill = "black")
	else:
		c.create_rectangle (50 * k, 50 * l, 50 * (k + 1), 50 * (l + 1), fill = "white")
for k in range (1, 9):
	for l in range (1, 9):
		draw_cell (k, l)
m = i
n = j
for i in range (1, 9):
	c.create_rectangle (50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill = "green")
for j in range (1, 9):
	c.create_rectangle (50 * m, 50 * j, 50 * (m + 1), 50 * (j + 1), fill = "green")
draw_cell (m, n)
c.mainloop()