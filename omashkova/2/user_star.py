import tkinter
c = tkinter. Canvas (width = 500, height = 500)
c.pack()
x = int(input())
y = int(input())
c.create_line (x, y, x + 10, y - 20, x + 20, y, x - 10, y - 10, x + 30, y - 10, x, y)
c.mainloop()
