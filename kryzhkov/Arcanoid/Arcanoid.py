import tkinter
import sys
import random
from collections import namedtuple
 
WIDTH=660
HEIGHT=660
FPS = 1000
RADIUS = 1000
 
 
Point = namedtuple("Point", ["x", "y"])
Game = namedtuple("Game", ["position", "direction","blocks","field"])

def draw_field(canvas, game):
  cell_width = WIDTH // 21
  cell_height = cell_width
  canvas.delete(*canvas.find_all())
  canvas.create_oval(
      game.position.x-RADIUS,
      game.position.y-RADIUS,
      game.position.x+RADIUS,
      game.position.y+RADIUS,
      fill="red")
  def draw_cell(point, color):
    canvas.create_rectangle(
        cell_width * point.x,
        cell_height * point.y,
        cell_width * (point.x + 1),
        cell_height * (point.y + 1),
        fill=color)

  canvas.delete(*canvas.find_all())

  for i in range(21):
    for j in range(3):
      draw_cell(Point(i, j),"white")
  for p in game.blocks:
    draw_cell(p, "blue")
  
def make_move(game):
  position = Point(
      game.position.x + game.direction.x,
      game.position.y + game.direction.y)
  direction = game.direction
  blocks = game.blocks
  field = game.field
  if not (RADIUS < position.x < WIDTH-RADIUS):
    direction = direction._replace(x=-direction.x)
  if not (RADIUS < position.y < HEIGHT-RADIUS):
    direction = direction._replace(y=-direction.y)
  if  (position.y+RADIUS in game.blocks) and not position.y+RADIUS in game.field:
    direction = direction._replace(y=-direction.y)
    return game._replace(
      blocks=(game.blocks - frozenset([position])),

      field=(position,) + game.field)
  if  position.y-RADIUS in game.blocks and not position.y-RADIUS in game.field:
    direction = direction._replace(y=-direction.y)
    return game._replace(
      blocks=(game.blocks - frozenset([position])),

      field=(position,) + game.field)
  if  position.x+RADIUS in game.blocks and not position.x+RADIUS in game.field:
    direction = direction._replace(x=-direction.x)
    return game._replace(
      blocks=(game.blocks - frozenset([position])),

      field=(position,) + game.field)
  if  position.x-RADIUS in game.blocks and not position.x-RADIUS in game.field:
    direction = direction._replace(x=-direction.x)
    return game._replace(
      blocks=(game.blocks - frozenset([position])),
      field=(position,) + game.field)
  return Game(position, direction,blocks,field)
 
        
 


c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
c.pack()
c.focus_set()
 
 
def loop():
  draw_field(c, loop.game)
  loop.game = make_move(loop.game)
  c.after(1000 // FPS, loop)
 
loop.game = Game(Point(WIDTH/2,HEIGHT/2), 
    Point(1,2),
    blocks=(
        [Point(x, y)
        for y in range(3)
          for x in range(21)]),
    field=frozenset())
 
loop()
c.mainloop()

