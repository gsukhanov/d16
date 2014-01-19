import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1
#constants
N = 15
SQUARE = 45 
M = 29
p = 22.5
#variables
previous_color = 'black'
v = 0
#arrays
whitex = []
blackx = []
whitey = []
blacky = []
#field
for x in range(0, N * SQUARE, SQUARE):
	for y in range(0, N * SQUARE, SQUARE):
		c.create_rectangle( x , y , x + SQUARE,  y + SQUARE, fill = "saddle brown")

#functions

def coordinate(m, k):
    m =  m // p
    k = k // p
    return m, k

def change_into_white():
    global previous_color
    previous_color = 'white'
    
def change_into_black():
    global previous_color
    previous_color = 'black'
    

def location(event): 
    c = event.widget 
    global v
    for k in range(M + 1):
        for z in range(M + 1):
            xy = coordinate(event.x, event.y)
            if xy[0] == k and xy[1] == z  :
                print(xy[0], xy[1], k, z)
                c.create_oval(((k/2 - 1) * SQUARE + SQUARE/2) , ( (z/2 -1) * SQUARE + SQUARE/2), ( ( k/2 + 1) * SQUARE - SQUARE/2),((z/2 + 1) * SQUARE - SQUARE/2), fill = previous_color)
                v = v + 1
                if v % 2 == 1:
                    change_into_white()
                else:
                    change_into_black()
def move(event): 
    c = event.widget 
    location(event)
                


c.bind("<Button-1>", move) 
 
c.mainloop()
