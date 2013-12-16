from tkinter import Canvas;
canvas = Canvas(width=1000,height=1000);
canvas.pack()
deleteList = [];
board = [];
nboard = [];
for x in range(100):
    row = []
    nrow = []
    for y in range(100):
        row.append(0);
        nrow.append(0);
    board.append(row);
    nboard.append(nrow);

state = False;
kSize=10;
for x in range(100):
    for y in range(100):
        canvas.create_rectangle(kSize*x, kSize*y, kSize*(x+1), kSize*(y+1));

def r():
    for item in deleteList:
        canvas.delete(item);
    for x in range(100):
        for y in range(100):
            if board[x][y] == 1:
                deleteList.append(canvas.create_rectangle(kSize*x, kSize*y, kSize*(x+1), kSize*(y+1), fill = 'cyan'));
def b(event):
    x = event.x//kSize;
    y = event.y//kSize;
    if board[x][y] == 1:
        board[x][y] = 0;
    else:
        board[x][y] = 1;
    r();

def c():
    global board;
    global nboard;
    for x in range(100):
        for y in range(100):
            ctr = 0
            if x == 0:
                xminus = 99;
            else:
                xminus = x-1;
            if y == 0:
                yminus = 99;
            else:
                yminus = y-1;
            if x == 99:
                xplus = 0;
            else:
                xplus = x+1;
            if y == 99:
                yplus = 0;
            else:
                yplus = y+1;
            if board[xplus][yplus] == 1:
                ctr += 1;
            if board[xplus][y] == 1:
                ctr += 1;
            if board[xplus][yminus] == 1:
                ctr += 1;
            if board[x][yplus] == 1:
                ctr += 1;
            if board[x][yminus] == 1:
                ctr += 1;
            if board[xminus][yplus] == 1:
                ctr += 1;
            if board[xminus][y] == 1:
                ctr += 1;
            if board[xminus][yminus] == 1:
                ctr += 1;
            if ctr == 3:
                nboard[x][y] = 1;
            elif ctr != 2:
                nboard[x][y] = 0;
            else:
                nboard[x][y] = board[x][y]
    board, nboard = nboard, board;
    
def l(*args):
    if state:
        c();
        r();
        canvas.after(10, func=l);

def s(*args):
    global state;
    state = not state;
    if state:
        l();
    
    
canvas.bind("<Button-1>",b);
canvas.bind("<Button-3>",s);
canvas.mainloop();
