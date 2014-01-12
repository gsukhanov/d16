import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1
#constants
N = 15
SQUARE = 45 
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
def change_into_white():
    global previous_color
    previous_color = 'white'
    
def change_into_black():
    global previous_color
    previous_color = 'black'

def vertical_match(x,y):
    k = 1
    for n in range (len(x) - 1):
        for m in range (k):
            if x[n] == x[m] and n != m:
                k = k + 1
                if k == 5:
                    text = c.create_text(700, 100, text = 'you win', fill = "red")
                    print(text)

def horizontal_match(x,y):
    k = 1
    for n in range (len(y) - 1):
        for m in range (k):
            if y[n] == y[m] and n != m:
                k = k + 1
                if k == 5:
                    text = c.create_text(700, 100, text = 'you win', fill = "red")
                    print(text)

def diagonal_match(x,y):
    k = 1
    

def location(event): 
    c = event.widget 
    global v
    for k in range(N):
        for z in range(N):
            if event.x > (k * SQUARE)  and event.x < ((k + 1) * SQUARE) and event.y > ( z * SQUARE)  and event.y < ((z + 1) * SQUARE):
                c.create_oval(((k - 1) * SQUARE + SQUARE/2) , ( (z -1) * SQUARE + SQUARE/2), ( (k + 1) * SQUARE - SQUARE/2),((z + 1) * SQUARE - SQUARE/2) , fill = previous_color)
                v = v + 1
                if v % 2 == 1:
                    blackx.append(k * 45)
                    blacky.append(z * 45)
                    change_into_white()
                    vertical_match(blackx, blacky)
                    horizontal_match(blackx, blacky)
                    print(blackx)
                    print(blacky)
                else:
                    whitex.append(k * 45)
                    whitey.append(z * 45)
                    change_into_black()
                    vertical_match(whitex, whitey)
                    al_match(whitex, whitey)
                    print(whitex)
                    print(whitey)
def move(event): 
    c = event.widget 
    location(event)
                


c.bind("<Button-1>", move) 
 
c.mainloop()
