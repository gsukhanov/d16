import turtle
N = 1000000
SCALE = 1000

turtle.speed('fastest')
for i in range(1, N):
    turtle.left(i**2)
    turtle.forward(i / SCALE)

