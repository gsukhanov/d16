import tkinter
def right_arrow(canvas, x, y):
	canvas.create_line(x, y, x + 20, y, x + 15, y - 4)
	canvas.create_line(x + 20, y, x + 15, y + 4)	
def left_arrow(canvas, x, y):
	canvas.create_line(x, y, x - 20, y, x - 15, y - 4)
	canvas.create_line(x - 20, y, x - 15, y + 4)
def drawing(canvas, soldiers):
	for n in range (len(soldiers) - 1):
		if soldiers[n] == "1":
			right_arrow(canvas, 30 * (n + 1) - 5, 20)
		else:
			left_arrow(canvas, 30 * (n + 1) + 5, 20)
def turning(canvas, soldiers):
	canvas.delete("all")
	global seconds
	seconds += 1
	face_to_face = []
	turn_in_process = False
	for n in range (len(soldiers) - 1):
		if soldiers[n] == "1" and soldiers[n+1] == "0":
			face_to_face.append(n)
			face_to_face.append(n+1)
			turn_in_process = True
	for d in face_to_face:
		soldiers[d] = str(1 - int(soldiers[d]))
	drawing(canvas, soldiers)
	if turn_in_process == True:
 		c.after(1000, turning, canvas, soldiers)
c = tkinter.Canvas (width = 1000, height = 1000)
c.pack()
soldiers = list(input())
global seconds
seconds = 0
turning(c, soldiers)
c.mainloop()
