import tkinter
import sys
import random
from collections import namedtuple
 
WIDTH=660
HEIGHT=660
FPS = 1000
RADIUS = 1
COUNT_WIDTH = 22
KOLVOHEIGHT = 3
cell_width = WIDTH // COUNT_WIDTH
cell_height = cell_width
 
Point = namedtuple("Point", ["x", "y"])
Game = namedtuple("Game", ["position", "direction","blocks"])     

def in_block(block, position):
  x0 = block.x * cell_width
  x1 = x0 + cell_width
  y0 = block.y * cell_width
  y1 = y0 + cell_width
  if (x0 < position.x+RADIUS < x1) and (y0 < position.y < y1) or (x0 < position.x-RADIUS < x1) and (y0 < position.y < y1):
    return "horizontal"
  elif (x0 < position.x < x1) and (y0 < position.y+RADIUS < y1) or (x0 < position.x < x1) and (y0 < position.y-RADIUS < y1):
    return "vertical"
  else:
    return None
def out_of_field(position):
  if not (RADIUS < position.x < WIDTH-RADIUS):
    return  "horizontal"
  if not (RADIUS < position.y < HEIGHT-RADIUS):
    return "vertical"
  else:
    return None

def draw_field(canvas, game):

  canvas.delete(*canvas.find_all())
  canvas.create_oval(
      game.position.x-RADIUS,
      game.position.y-RADIUS,
      game.position.x+RADIUS,
      game.position.y+RADIUS,fill="red")
  def draw_cell(point, color):
    canvas.create_rectangle(
        cell_width * point.x,
        cell_height * point.y,
        cell_width * (point.x + 1),
        cell_height * (point.y + 1),
        fill=color)

  for i in range(COUNT_WIDTH):
    for j in range(KOLVOHEIGHT):
      draw_cell(Point(i, j),"white")
  for p in game.blocks:
    draw_cell(p, "blue")
  
def make_move(game):
  position = Point(
      game.position.x + game.direction.x,
      game.position.y + game.direction.y)
  direction = game.direction
  blocks = game.blocks
  move = out_of_field(position)
  if move == "vertical":
    direction = direction._replace(y=-direction.y)
  if move == "horizontal":
    direction = direction._replace(x=-direction.x)
  for y in range(3):
    for x in range(22):
      in_block(blocks[x,y],position)
      if in_block == "vertical":
        direction = direction._replace(y=-direction.y)
        return Game(
              position = position,
              direction = direction,
              blocks = game.blocks - frozenset([x.y])) 
      elif  in_block() == "horizontal" :
        direction = direction._replace(x=-direction.x)
        return Game(
              position = position,
              direction = direction,
              blocks = game.blocks - frozenset([x.y]))   

  return Game(
        position = position,
        direction = direction,
        blocks = blocks)
 
        
c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
c.pack()
c.focus_set()
 
 
def loop():
  draw_field(c, loop.game)
  loop.game = make_move(loop.game)
  c.after(1000 // FPS, loop)
 
loop.game = Game(Point(WIDTH/2,HEIGHT/2),
    Point(1,2),
    blocks = frozenset(
        [Point(x, y)
        for y in range(3)
          for x in range(22)]))
 
loop()
c.mainloop()