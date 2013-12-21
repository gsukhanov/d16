import tkinter
c = tkinter. Canvas (width=600, height=600)
c.pack()
def draw_line(event):
	c.create_line (0, 0, event.x, event.y)
c.bind("<Motion>", draw_line)
c.mainloop()