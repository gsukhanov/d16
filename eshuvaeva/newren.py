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
black = []

#field
for x in range(0, N * SQUARE, SQUARE):
    for y in range(0, N * SQUARE, SQUARE):
        c.create_rectangle( x , y , x + SQUARE,  y + SQUARE, fill = "saddle brown")

#temporary functions

def write(event): #эта функция и будет вызываться. На вход ей будет подаваться информация о событии
    c = event.widget #в частности, передаётся ссылка на объект
    c.create_text(event.x, event.y, text=coordinate(event.x, event.y)) 
def last(k, z):
    if k == 28:
        k = k -1
    if z == 28:
        z = z - 1
    return(k,z)
def first(k, z):
    if k == 0:
        k = k + 1
    if z == 0:
        z = z + 1
    return(k,z)

#functions
def coordinate(m, k):
    m =  m // p
    k = k // p
    return m, k


def vertical_match(array):
    for i in range(len(array)):
        h = 1
        for j in range(len(array)):
            if array[i][0] == array[j][0] and i != j:
                h = h + 1
                if h == 5:
                    text = c.create_text(700, 100, text = 'you win', fill = "red")
def horizontal_match(array):
    for i in range(len(array)):
        h = 1
        for j in range(len(array)):
            m = following_pieces(array)
            if array[i][1] == array[j][1] and i != j and m == 5:
                h = h + 1
                if h == 5:
                    text = c.create_text(700, 100, text = 'you win', fill = "red")
def following_pieces(array):
    for i in range(1,len(array),1):
        k = 0
        for j in range(1, len(array), 1):
            if j == i + 1 or i == j + 1:
                k = k + 1
    return(k)







def location(event): 
    c = event.widget 
    global v
    for k in range(M ):
        for z in range(M ):
            xy = coordinate(event.x, event.y)
            a = xy[0] // 2
            b = xy[1] // 2
            inside = []
            inside.append(a)
            inside.append(b)
            if xy[0] == k and xy[1] == z : 
                one = (k/2*SQUARE + SQUARE/2) // SQUARE
                two = (z/2*SQUARE + SQUARE/2) // SQUARE
                c.create_oval((one * SQUARE  - SQUARE/2 ) , ( two * SQUARE - SQUARE/2 ), (one * SQUARE + SQUARE/2),( two * SQUARE + SQUARE/2), fill = previous_color)
                black.append(inside)
                print((k/2*SQUARE + SQUARE/2) // SQUARE) 
                print((z/2*SQUARE + SQUARE/2) // SQUARE )
                vertical_match(black)
                horizontal_match(black)
def move(event): 
    c = event.widget 
    location(event)
                


c.bind("<Button-1>", move) 

c.bind("<Button-3>", write) 
c.mainloop()







