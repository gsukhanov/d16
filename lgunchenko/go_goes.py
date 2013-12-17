import tkinter
n = 12
CELL_SIZE = 35
c = tkinter.Canvas( width = 1000, height = 600)
c.pack()
for x in range (0, n*CELL_SIZE, CELL_SIZE):
        for y in range (0,n*CELL_SIZE, CELL_SIZE):
                color = "brown"
                c.create_rectangle (x+50, y+100, x+50+CELL_SIZE, y+100+CELL_SIZE, fill = color)
player = "black"
A = [[""]* n for i in range(n)]

def move(event):
        global player
        c = event.widget
        if player == "black":

                if A[event.x // CELL_SIZE][event.y // CELL_SIZE] == "":
                        A[event.x // CELL_SIZE][event.y // CELL_SIZE] = "black" 
                        player = "white"     
        else: 
                if A[event.x // CELL_SIZE][event.y // CELL_SIZE] == "":
                
                        A[event.x // CELL_SIZE][event.y // CELL_SIZE] = "white"
                        player = "black"
        x = (event.x)// CELL_SIZE 
        y = (event.y)// CELL_SIZE
        print(x,y)
        if 1<=x<=13 and 2<=y<=14:
                c.create_oval(x * CELL_SIZE , y * CELL_SIZE +15, x * CELL_SIZE +30, y * CELL_SIZE+45 , fill = player)
        else:
                exit(0)


c.bind("<Button-1>", move)
c.mainloop()
