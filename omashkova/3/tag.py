import tkinter
import random
global c
global my_map
my_map = []
c = tkinter. Canvas (width=500, height=500)
c.pack()
def draw_cell (canvas, i, j, number):
	canvas.create_rectangle (50 * i + 10, 50 * j + 10, 50 * (i + 1) + 10, 50 * (j + 1) + 10)
	canvas.create_text ((50 * i) + 35, (50 * j) + 35, text = number)
def print_my_map (canvas, my_map):
	for i in range (len(my_map)):
		for j in range (len(my_map)):
			if my_map[i][j] != 0:
				draw_cell (canvas, i, j, my_map[i][j])
def random_fill_my_map (my_map):
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	for i in range (4):
		temp_array=[]
		for j in range (4):
			random_index = random.randint (0, len(numbers) - 1) 
			temp_array.append(numbers[random_index])
			del numbers[random_index]
		my_map.append(temp_array)
def move (i, j, my_map):
	l = j
	k = i - 1
	if (k >= 0) and (l >= 0) and (k < 4) and (l < 4):
		if my_map[k][l] == 0:
			my_map[k][l], my_map[i][j] = my_map[i][j], my_map[k][l]
			return
	l = j
	k = i + 1
	if (k >= 0) and (l >= 0) and (k < 4) and (l < 4):
		if my_map[k][l] == 0:
			my_map[k][l], my_map[i][j] = my_map[i][j], my_map[k][l]
			return
	l = j - 1
	k = i
	if (k >= 0) and (l >= 0) and (k < 4) and (l < 4):
		if my_map[k][l] == 0:
			my_map[k][l], my_map[i][j] = my_map[i][j], my_map[k][l]
			return
	l = j + 1
	k = i
	if (k >= 0) and (l >= 0) and (k < 4) and (l < 4):
		if my_map[k][l] == 0:
			my_map[k][l], my_map[i][j] = my_map[i][j], my_map[k][l]
			return								
def mouse_click_reaction (event):
	global c
	global my_map
	i = (event.x - 10) // 50
	j = (event.y - 10) // 50
	c.delete("all")
	move (i, j, my_map)
	print_my_map (c, my_map)
c.bind ("<Button-1>", mouse_click_reaction)		
random_fill_my_map (my_map)
print_my_map (c, my_map)
c.mainloop()
