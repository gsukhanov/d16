b = int(input())
a = int(input())
n = int(input())





import tkinter
import random
size = 50
c=tkinter.Canvas(width=size*a,height=size*b)
c.pack()








BOMB=9





def create_bombs(n, a, b):   # n - кол-во бомб; a - кол-во клеток по горизонтали; b - по вертикали
    m = []
    for x in range(n):
        k = (random.randrange(a * b))
        while k in m:
                k = (random.randrange(a * b))
        m.append (k)
    return m



def schet (t):
    if t in m:
        c = c + 1
    return c


q = [0] * a
array2d = [q] * b
for p in (a * b)
    d = p//a
    m = p - d * a
        if p in m:
            array2d[d][m] = BOMB
        else:
            c = 0
            schet (p + 1)
            schet (p - 1)
            schet (p + a)
            schet (p - a)
            schet (p + 1 + a)
            schet (p + 1 - a)
            schet (p - 1 - a)
            schet (p - 1 + a)
            array2d[d][m] = c







c.bind("<Button-1>", write_coordinates)
def write_coordinates(event): 
    i = event.y//size
    j = event.x//size
    n = a[i][j]
    c.create_text(j*size - size/2, i*size - size/2, text=n)
    if n == 0:
        r.append (i) 
        v.append (j)
            while len(r) != 0                      # мы решаем проблему с пустыми клетками
                i = r.pop(0)
                j = v.pop(0)
                for dx in range(i - 1, i + 1):
                    for dy in range(j - 1, j + 1):
                        n = a[i][j]
                        c.create_text(j*size - size/2, i*size - size/2, text=n)
                    if n == 0:
                        if not(i in r and j in v):
                            r.append (i) 
                            v.append (j)
