
n = 5
a = 4
b = 2

import random

BOMB=9




def create_bombs(n, a, b):   # n - кол-во бомб; a - кол-во клеток по горизонтали; b - по вертикали
    m = []
    for x in range(n):
        k = (random.randrange(a * b))

        while k in m:
                k = (random.randrange(a * b))
        m.append (k)
    return m

m = create_bombs(n, a, b)

print (m)

def schet (t):
    global c
    if t in m:
        c = c + 1
    return c


q = [0] * a
array2d = [q] * b
for p in range(a * b):
    d = p//a
    u = p - d * a
    if p in m:
        array2d[d][u] = BOMB
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
        array2d[d][u] = c


print (array2d)