import tkinter
CELL_SIZE = 35
SHIFT = 50
SIZE = 12
RADIUS = 12.5
c = tkinter.Canvas( width = 1000, height = 600)
c.pack()
for x in range (0, SIZE*CELL_SIZE, CELL_SIZE):
        for y in range (0,SIZE*CELL_SIZE, CELL_SIZE):
                color = "brown"
                c.create_rectangle (x+SHIFT, y+SHIFT, x+SHIFT+CELL_SIZE, y+SHIFT+CELL_SIZE, fill = color)
player = "black"

A = [[""] * (SIZE+1) for x in range(SIZE+1)]


def to_screen(c):
        return c * CELL_SIZE + SHIFT
def from_screen(c):
        return (c - SHIFT) // CELL_SIZE
def move(event):
        x = from_screen(event.x)
        y = from_screen(event.y)
        if x< 0 or x>SIZE or y< 0  or y>SIZE:
                return
  
        else:                           
                global player
                c = event.widget
                if player == "black":
                        
                        if A [x][y] == "":
                                A[x][y] = player
                                player = "white"
                        else:
                                return


                else:
                        if A[x][y] == "":
                                A[x][y] = player
                                player = "black"
                        else:
                                return
                  

        c.create_oval(to_screen(x)-RADIUS , to_screen(y)-RADIUS, to_screen(x)+RADIUS, to_screen(y)+RADIUS , fill = player)
c.bind("<Button-1>", move)
c.mainloop()
