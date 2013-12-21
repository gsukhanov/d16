import tkinter
import sys
import random
import math
from collections import namedtuple

WIDTH=440
HEIGHT=660
FPS = 1000
RADIUS = [10,10,10,10,10,10,10]
HOLE_FILL='black'
FIELD_COLOR='green'
BORDER_COLOR='dark green'
HOLE_RADIUS=[33,24]
r=17
R=10
a=90
V1=[3,2,3,4,5,5,6]
A1=[0.001,0.002,0.003,0.004,0.005,0.004,0.009]
A2=[0.00001,0.00002,0.00003,0.00004,0.00005,0.00006,0.00007]
A3=[1,1,1,1,1,1,1]
V2=[1.1,0.2,0.3,0.4,0.5,0.6,0.57]
V0=[0,0,0,0,0,0,0]
A0=[0,0,0,0,0,0,0]
V3=[3,3,3,3,3,3]
V4=[30,30,30,30,30,30]
A4=[-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001]
v=V2
a=A0
FILL=['red','blue','white','brown','yellow','orange','grey']
FILL1=['white','white','white','white','white','white','red']
fill=FILL

Point = namedtuple("Point", ["x", "y"])
Ball = namedtuple("Game", ["position", "angle","active"])
HOLES=[(-HOLE_RADIUS[0],-HOLE_RADIUS[0],HOLE_RADIUS[0],HOLE_RADIUS[0]),
       (WIDTH-HOLE_RADIUS[0],-HOLE_RADIUS[0],WIDTH+HOLE_RADIUS[0],HOLE_RADIUS[0]),
       (-HOLE_RADIUS[0],HEIGHT-HOLE_RADIUS[0],HOLE_RADIUS[0],HEIGHT+HOLE_RADIUS[0]),
       (WIDTH-HOLE_RADIUS[0],HEIGHT-HOLE_RADIUS[0],WIDTH+HOLE_RADIUS[0],HEIGHT+HOLE_RADIUS[0]),
       (-HOLE_RADIUS[1],HEIGHT//2-HOLE_RADIUS[1],HOLE_RADIUS[1],HEIGHT//2+HOLE_RADIUS[1]),
       (WIDTH-HOLE_RADIUS[1],HEIGHT//2-HOLE_RADIUS[1],WIDTH+HOLE_RADIUS[1],HEIGHT//2+HOLE_RADIUS[1])]

def draw_field(canvas,lgame):
  canvas.delete(*canvas.find_all())
  canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill=BORDER_COLOR)
  canvas.create_rectangle(5,5,WIDTH-5, HEIGHT-5, fill=FIELD_COLOR)
  for i in range(len(HOLES)):
    canvas.create_oval(HOLES[i][0],HOLES[i][1],HOLES[i][2],HOLES[i][3],fill=HOLE_FILL)
  for i in range(0,len(lgame)):
    if lgame[i].active:
      canvas.create_oval(
        lgame[i].position.x-RADIUS[i],
        lgame[i].position.y-RADIUS[i],
        lgame[i].position.x+RADIUS[i],
        lgame[i].position.y+RADIUS[i],
        fill=fill[i])
def distance (x1,y1,x2,y2):
  return ((x1-x2)**2+(y1-y2)**2)**0.5
def make_move(lgame,number):
  game=lgame[number]
  angle=game.angle
  global v
  dx=math.cos(game.angle/57.295779513)
  dy=-math.sin(game.angle/57.295779513)
  position = Point(
      game.position.x + (dx*v[number])*bool(v[number]>=0),
      game.position.y + (dy*v[number])*bool(v[number]>=0))
  direction = [dx,dy]
  if not (RADIUS[number] < position.x < WIDTH-RADIUS[number]-5):
    angle=180-angle
  if not (RADIUS[number] < position.y < HEIGHT-RADIUS[number]-5):
    angle=-angle
  for i in range(0,len(lgame)):
    x=position.x
    y=position.y
    x1=lgame[i].position.x
    y1=lgame[i].position.y
    if  (((x-x1)**2+(y-y1)**2)**0.5)<=20 and i!=number and lgame[i].active:
        angle+=180
        lgame[i] = lgame[i]._replace(angle = lgame[i].angle+180)
  v[number]+=a[number]
  active=True
  for i in range(0,len(HOLES)):
    if distance(position.x, position.y, (HOLES[i][0]+HOLES[i][2])/2,(HOLES[i][1]+HOLES[i][3])/2)<=HOLE_RADIUS[1]*0.9*(bool(i>=4))+HOLE_RADIUS[0]*0.9*(bool(i<4)):
      active=False
  angle+=0
  return Ball(position, angle,active)


if __name__ == "__main__":
  c = tkinter.Canvas(width=WIDTH-2, height=HEIGHT-2)
  c.pack()
  c.focus_set()
def loop():
  global lgame
  draw_field(c, lgame)
  for i in range(0,len(lgame)):
      lgame[i] = make_move(lgame,i)
      if not lgame[i].active:
          v[i]=0
          a[i]=0
  c.after(1000 // FPS, loop)
lgame = [Ball(Point(WIDTH/2,HEIGHT/3), 10,True),
        Ball(Point(WIDTH/2-2*r,HEIGHT/3-2*r), 20,True),
        Ball(Point(WIDTH/2+2*r,HEIGHT/3-2*r), 30,True),
        Ball(Point(WIDTH/2-r,HEIGHT/3-r), 40,True),
        Ball(Point(WIDTH/2+r,HEIGHT/3-r), 50,True),
        Ball(Point(WIDTH/2,HEIGHT/3-2*r), 60,True),
        Ball(Point(WIDTH*0.5,HEIGHT*0.7), 70,True)]
loop()
c.mainloop()
