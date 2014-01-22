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
    for k in range(M ):
        for z in range(M ):
            xy = coordinate(event.x, event.y)
            if xy[0] == k and xy[1] == z  :

                if k % 2 == 0 and z % 2 == 0:
                    c.create_oval(((k/2 - 0.5) * SQUARE) , ( (z/2 -0.5) * SQUARE ), ( ( k/2 + 0.5) * SQUARE),((z/2 + 0.5) * SQUARE ), fill = previous_color)

                if k % 2 == 1 and z % 2 == 0:
                    c.create_oval((((k -1)/2 + 0.5) * SQUARE) , ( (z/2 -0.5) * SQUARE ), ( ( (k - 1)/2 + 1.5) * SQUARE),((z/2 + 0.5) * SQUARE), fill = previous_color)
                    print((k/2 + 0.5) * SQUARE, (k/2 + 1.5) * SQUARE)
                if k % 2 == 0 and z % 2 == 1:
                    c.create_oval(((k/2 - 0.5) * SQUARE) , ( ((z - 1)/2 + 0.5) * SQUARE), ( ( k/2 + 0.5) * SQUARE),(((z - 1)/2 + 1.5) * SQUARE), fill = previous_color)
                
                if k % 2 == 1 and z % 2 == 1:
                    c.create_oval((((k - 1)/2 + 0.5) * SQUARE) , ( ((z - 1)/2 + 0.5) * SQUARE ), ( (( k - 1)/2 + 1.5) * SQUARE ),(((z - 1)/2 + 1.5) * SQUARE), fill = previous_color)
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

