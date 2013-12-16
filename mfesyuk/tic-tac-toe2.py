import tkinter
n = 3
p = 100
c = tkinter.Canvas(width = p * n, height = p * n)
c.pack()
for i in range(0, p * n, p):
        c.create_line(0, i, p * n, i)
for i in range(0, p * n, p):
        c.create_line(i, 0, i, p * n)
field = [[""] * n for i in range(n)]
player = "cross"
def move(event):
        global player
        c = event.widget
        if player == "cross":
                if field[event.x // p][event.y // p] == "":
                        c.create_line(event.x // p * p, event.y // p * p + p, event.x // p * p + p, event.y // p * p)
                        c.create_line(event.x // p * p, event.y // p * p, event.x // p * p + p, event.y // p * p + p)
                        field[event.x // p][event.y // p] = "cross"
        else:
                if field[event.x // p][event.y // p] == "":
                        c = event.widget
                        c.create_oval(event.x // p * p, event.y // p * p, event.x // p * p + p, event.y // p * p + p)
                        field[event.x // p][event.y // p] = "zero"
        for i in range(n):
                s = 0
                for j in range(n):
                        if field[i][j] == player:
                                s += 1
                if s == n:
                        c.create_line(p * j + p // 2, 0, p * j + p // 2, n)
                        if player == "cross":
                                c.create_text(p // 2, p, text="Cross win!")
                        else:
                                c.create_text(p // 2, p, text="Zero win")
                        exit(0)
        # 2: для столбца
        for j in range(n):
                s = 0
                for i in range(n):
                        if field[i][j] == player:
                                s += 1
                if s == n:
                        c.create_line(0, p * i + 50, p * n, p * i + p // 2)
                        if player == "cross":
                                c.create_text(p // 2, p, text="Cross win!")
                        else:
                                c.create_text(p // 2, p, text="Zero win")
                        exit(0)
        # 3: для диагонали(л-в - п-н)
        s = 0
        for i in range(n):
                for j in range(n):
                        if field[i][j] == player:
                                if i == j:
                                        s += 1
        if s == n:
                c.create_line(0, 0, n, n)
                if player == "cross":
                        c.create_text(p // 2, p, text="Cross win!")
                else:
                        c.create_text(p // 2, p, text="Zero win")
                exit(0)
        # 4: для диагонали(л-н - п-в)
        s = 0
        for i in range(n):
                for j in range(n):
                        if field[i][j] == player:
                                if i + j == n:
                                        s += 1
        if s == n:
                c.create_line(0, n, n, 0)
                if player == "cross":
                        c.create_text(p // 2, p, text="Cross win!")
                else:
                        c.create_text(p // 2, p, text="Zero win")
                exit(0)
        if player == "cross":
                player = "zero"
        else:
                player = "cross"
c.bind("<Button-1>", move)
c.mainloop()
