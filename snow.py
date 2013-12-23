import tkinter 
import random
from collections import namedtuple

WIDTH = 1300
HEIGHT = 800
RADIUS = 2
FLAKES_COUNT = 500
SPEED = 1

Point = namedtuple("Point", ["x", "y"])

snow = []
for i in range(FLAKES_COUNT):
	snow.append(Point(random.randrange(WIDTH), random.randrange(HEIGHT)))

c=tkinter.Canvas(width=WIDTH,height=HEIGHT)
c.focus_set()

def draw_snowflake(x, y):
	c.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill="white")

def draw():
	c.delete(*c.find_all())
	for s in snow:
		draw_snowflake(s.x, s.y)

def move():
	for i in range(len(snow)):
		dx = random.randrange(0,SPEED+1)
		dy = random.randrange(SPEED+1,2*SPEED+1)
		snow[i] = Point(
				(snow[i].x + dx + WIDTH) % WIDTH,
				(snow[i].y + dy + HEIGHT) % HEIGHT)

def loop():
	draw()
	move()
	c.after(100, loop)


def key_press(event):
	global SPEED
	print(event.keysym)
	if event.keysym == "plus":
		SPEED += 1
	if event.keysym == "minus":
		SPEED -= 1


c.bind("<Key>", key_press)
loop()
c.pack()
c.mainloop()
