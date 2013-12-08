import tkinter
def prosto(): 
  c.delete(*c.find_all())
  x = 100
  y = 0
  z = 0
  while y < n - 1:
    if A[y] < A[y + 1]:
      A[y] = 1
      A[y + 1] = 0
      y += 1
      z += 1
    y += 1
  x = 10
  for i in range(n):
    if A[i] == 0:
      c.create_text (x + 25 * i, y, text = "-->")
    if A[i] == 1:
      c.create_text (x + 25 * i, y, text = "<--")
  if z > 0:
    c.after(1000, prosto)
  else:
    c.create_text(50,100, text = "You win!")
    return
c = tkinter.Canvas(width = 1000, height = 600)
c.pack() 
n = int(input())
A = []
for i in range(n):
  A.append(int(input()))
prosto()

c.mainloop()
