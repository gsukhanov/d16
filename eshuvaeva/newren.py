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
color = 'black'
v = 0
#arrays
white = []
black = []
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
    global color
    color = 'white'
    
def change_into_black():
    global color
    color = 'black'

def vertical_match(array):
    for i in range(0, len(array), 2):
        k = array[i]
        j = array.count(k)
        if j >= 5:
            text = c.create_text(700, 100, text = 'you win', fill = "red")
        print(j)


    

def location(event): 
    c = event.widget 
    global v
    for k in range(M ):
        for z in range(M ):
            xy = coordinate(event.x, event.y)
            a = xy[0] // 2
            if (a % 2 == 1 and color == 'black') or (a % 2 == 0 and color == 'white'):
                a = a + 1
            b = xy[1] // 2
            if (b % 2 == 1 and color == 'black') or (b % 2 == 0 and color == 'white'):
                b = b + 1
            if xy[0] == k and xy[1] == z : 
                one = (k/2*SQUARE + SQUARE/2) // SQUARE
                two = (z/2*SQUARE + SQUARE/2) // SQUARE
                c.create_oval((one * SQUARE  - SQUARE/2 ) , ( two * SQUARE - SQUARE/2 ), (one * SQUARE + SQUARE/2),( two * SQUARE + SQUARE/2), fill = color)
                v = v + 1
                if v % 2 == 1:
                    black.append(a)
                    black.append(b)
                    vertical_match(black)
                    change_into_white()
                else:
                    white.append(a)
                    white.append(b)
                    #vertical_match(white)
                    change_into_black()
                #print(black)
                #print(white) 
                
def move(event): 
    c = event.widget 
    location(event)
                


c.bind("<Button-1>", move) 
 
c.mainloop()








