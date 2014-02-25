import tkinter
c = tkinter.Canvas(width = 1000, height = 1000)
c.pack()
m = 3
def  gex(x, y, color):
    c.create_polygon(x - 10*m, y - 5*m, x , y - 10*m, x + 10*m, y - 5*m, x + 10*m, y + 5*m, x , y + 10*m, x - 10*m, y + 5*m, outline = "black", fill = color)
x = 10*m
h = 15*m
k = 11
l = x + 2*10*m*k
a = []
step = 1
while k > 0:
	r = []
	for o in range(x, l, 2*10*m):
		gex(o, h, "white")
		mass = [o, h]
		r.append(mass)
	a.append(r)
	x += 10*m
	l += 10*m
	h += 15*m
	k -= 1

redgexes = []
bluegexes = []

def point_inside_polygon(x,y,a,b):
    inside = False
    global m
    if x > a-10*m and x < a+10*m and y >= b - 5*m and y <= b+5*m:
    	inside = True
    if y < b-5*m and y > b -10*m and x >= a and x < a+10*m:
    	if x/2 + b - 10*m - a/2 < y:
    		inside = True
    if x >= a and x < a+10*m and y > b+5*m and y < b +10*m:
    	if -x/2 + b + 10*m + a/2 > y:
    		inside = True
    if x > a-10*m and x <= a and y < b-5*m and y > b -10*m:
    	if -x/2 + b - 10*m + a/2 < y:
    		inside = True
    if x > a-10*m and x <= a and y > b+5*m and y < b +10*m:
    	if x/2 +b + 10*m - a/2 > y:
    		inside = True
    return inside

def paint(event):
    global m
    global step
    g = 15*m
    ev = event.widget 
    screenx = event.x
    screeny = event.y
    ourgexx = None
    ourgexy = None
    for i in range(0, 11):
    	for t in range(0, 11):
    			nomerr = i
    			nomerm = t
    			one, two = a[i][t][0], a[i][t][1]
    			what = point_inside_polygon(screenx, screeny, one, two)
    			if what == True:
    				ourgexx = one
    				ourgexy = two

    				a[i][t][0] = 0
    				a[i][t][1] = 0
    if ourgexx is None or ourgexy is None:
    	print("Try again")
    else:
    	if step % 2 == 1:
    		gex(ourgexx, ourgexy, "red")
    		step += 1
    	else:
    		gex(ourgexx, ourgexy, "steel blue")
    		step += 1
    print(redgexes, bluegexes)



win = False
c.bind("<Button-1>", paint)

c.mainloop()