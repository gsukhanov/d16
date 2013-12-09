import tkinter
# игровой процесс:
n = int(input()) # n - кол-во клеток в строке и столбце (поле n*n)
c = tkinter.Canvas(width = 100 * n, height = 100 * n)
c.pack()
# создается поле n*n
for i in range(0, 100 * n, 100):
	c.create_line(0, i, 100 * n, i)
for i in range(0, 100 * n, 100):
	c.create_line(i, 0, i, 100 * n)
# создаются массивы A и B, в которые будут записываться в каком месте кто поставил крестик(А) или нолик(В)
A = [[0] * n for i in range(n)]
B = [[0] * n for i in range(n)]
# функция, кторая при нажатии рисует крестик или нолик, при этом записывая действия в созданные массивы
def tick(event):
	c = event.widget
	c.create_line(event.x // 100 * 100, event.y // 100 * 100, event.x // 100 * 100 + 100, event.y // 100 * 100 + 100)
	c.create_line(event.x // 100 * 100, event.y // 100 * 100 + 100, event.x // 100 * 100 + 100, event.y // 100 * 100)
	A[event.x // 100][event.y // 100] = 1
	for i in range(n):
		s = 0
		for j in range(n):
			s += A[i][j]
		if s == n:
			c.create_line(100 * j + 50, 0, 100 * j + 50, n)
			c.create_text(50, 100, text="Tick win!")
			return
	# 2: для столбца
	for j in range(n):
		s = 0
		for i in range(n):
			s += A[i][j]
		if s == n:
			c.create_line(0, 100 * i + 50, 100 * n, 100 * i + 50)
			c.create_text(50, 100, text="Tick win!")
			return
	# 3: для диагонали(л-в - п-н)
	s = 0
	for i in range(n):
		for j in range(n):
			if i == j:
				s += A[i][j]
	if s == n:
		c.create_line(0, 0, n, n)
		c.create_text(50, 100, text="Tick win!")
		return
	# 4: для диагонали(л-н - п-в)
	s = 0
	for i in range(n):
		for j in range(n):
			if i + j == n:
				s += A[i][j]
	if s == n:
		c.create_line(0, n, n, 0)
		c.create_text(50, 100, text="Tick win!")
		return
	# выиграли нолики
	# 1: для строки
	for i in range(n):
		s = 0
		for j in range(n):
			s += B[i][j]
		if s == n:
			c.create_line(100 * j + 50, 0, 100 * j + 50, n)
			c.create_text(50, 100, text="Zero win!")
			return
	# 2: для столбца
	for j in range(n):
		s = 0
		for i in range(n):
			s += B[i][j]
		if s == n:
			c.create_line(0, 100 * i + 50, 100 * n, 100 * i + 50)
			c.create_text(50, 100, text="Zero win!")
			return
	# 3: для диагонали(л-в - п-н)
	s = 0
	for i in range(n):
		for j in range(n):
			if i == j:
				s += B[i][j]
	if s == n:
		c.create_line(0, 0, n, n)
		c.create_text(50, 100, text="Zero win!")
		return
	# 4: для диагонали(л-н - п-в)
	s = 0
	for i in range(n):
		for j in range(n):
			if i + j == n:
				s += B[i][j]
	if s == n:
		c.create_line(0, n, n, 0)
		c.create_text(50, 100, text="Zero win!")
		return
def zero(event):
	c = event.widget
	c.create_oval(event.x // 100 * 100, event.y // 100 * 100, event.x // 100 * 100 + 100, event.y // 100 * 100 + 100)
	B[event.x // 100][event.y // 100] = 1
	for i in range(n):
		s = 0
		for j in range(n):
			s += A[i][j]
		if s == n:
			c.create_line(100 * j + 50, 0, 100 * j + 50, n)
			c.create_text(50, 100, text="Tick win!")
			return
	# 2: для столбца
	for j in range(n):
		s = 0
		for i in range(n):
			s += A[i][j]
		if s == n:
			c.create_line(0, 100 * i + 50, 100 * n, 100 * i + 50)
			c.create_text(50, 100, text="Tick win!")
			return
	# 3: для диагонали(л-в - п-н)
	s = 0
	for i in range(n):
		for j in range(n):
			if i == j:
				s += A[i][j]
	if s == n:
		c.create_line(0, 0, n, n)
		c.create_text(50, 100, text="Tick win!")
		return
	# 4: для диагонали(л-н - п-в)
	s = 0
	for i in range(n):
		for j in range(n):
			if i + j == n:
				s += A[i][j]
	if s == n:
		c.create_line(0, n, n, 0)
		c.create_text(50, 100, text="Tick win!")
		return
	# выиграли нолики
	# 1: для строки
	for i in range(n):
		s = 0
		for j in range(n):
			s += B[i][j]
		if s == n:
			c.create_line(100 * j + 50, 0, 100 * j + 50, n)
			c.create_text(50, 100, text="Zero win!")
			return
	# 2: для столбца
	for j in range(n):
		s = 0
		for i in range(n):
			s += B[i][j]
		if s == n:
			c.create_line(0, 100 * i + 50, 100 * n, 100 * i + 50)
			c.create_text(50, 100, text="Zero win!")
			return
	# 3: для диагонали(л-в - п-н)
	s = 0
	for i in range(n):
		for j in range(n):
			if i == j:
				s += B[i][j]
	if s == n:
		c.create_line(0, 0, n, n)
		c.create_text(50, 100, text="Zero win!")
		return
	# 4: для диагонали(л-н - п-в)
	s = 0
	for i in range(n):
		for j in range(n):
			if i + j == n:
				s += B[i][j]
	if s == n:
		c.create_line(0, n, n, 0)
		c.create_text(50, 100, text="Zero win!")
		return
c.bind("<Button-1>", tick)
c.bind("<Button-3>", zero)
c.mainloop()