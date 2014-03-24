import turtle as T

T.speed("fastest")
kLength = 200
kDepth = 3
kAngle = 60


def drawKoch(length, depth):
    if depth == 0:
        T.forward(length)
    else:
		newLen = length / 3
		drawKoch(newLen, depth-1)
		T.left(kAngle)
		drawKoch(newLen, depth-1)
		T.right(180 - kAngle)
		drawKoch(newLen, depth-1)
		T.left(kAngle)
		drawKoch(newLen, depth-1)
		
		

T.penup()
T.left(180)
T.forward(200)
T.left(180)
T.pendown()
drawKoch(kLength, kDepth)
T.right(120)
drawKoch(kLength, kDepth)
T.right(120)
drawKoch(kLength, kDepth)
