import tkinter
print("Input the size of field; 9/ 13/ 19")
size = int(input())
if size<9 or size>19 or 9<size<13 or 13<size<19:
        print("Wrong size, restart game")
        exit(0)

c = tkinter.Canvas( width = 2000, height = 2000)
c.pack()
for x in range (0, size*35, 35):
        for y in range (0,size*35, 35):
                if (x+y)%2 == 0:
                        color = "beige"
                else: 
                        color = "brown"
                c.create_rectangle (x+50, y+100, x+85, y+135, fill = color)
c.mainloop()