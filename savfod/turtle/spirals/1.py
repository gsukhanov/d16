import turtle
N = 1000000
SCALE = 100

turtle.speed('fastest')
for i in range(1, N):
    turtle.left(i)
    turtle.forward(i / SCALE)
