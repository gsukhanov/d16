import tkinter
c = tkinter. Canvas (width=500, height=500)
c.pack()
def draw_cell (i, j):
	if i % 2 == j % 2:
		c.create_rectangle (50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill = "black")
	else:
		c.create_rectangle (50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill = "white")
for i in range (1, 9):
	for j in range (1, 9):
		draw_cell (i, j)
	