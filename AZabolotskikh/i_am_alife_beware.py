from tkinter import Canvas;
import plistlib;
kSize=10;
kBoardWidth = kBoardHeight = 100;
canvas = Canvas(width=kBoardWidth*kSize,height=kBoardHeight*kSize);
canvas.pack();
deleteList = [];
board = [];
nboard = [];
for x in range(kBoardWidth):
	row = [];
	nrow = [];
	for y in range(kBoardHeight):
		row.append(0);
		nrow.append(0);
	board.append(row);
	nboard.append(nrow);

state = False;
for x in range(kBoardWidth):
	for y in range(kBoardHeight):
		canvas.create_rectangle(kSize*x, kSize*y, kSize*(x+1), kSize*(y+1));

def redraw():
	for item in deleteList:
		canvas.delete(item);
	del deleteList[:];
	for x in range(kBoardWidth):
		for y in range(kBoardHeight):
			if board[x][y] == 1:
				deleteList.append(canvas.create_rectangle(kSize*x, kSize*y, kSize*(x+1), kSize*(y+1), fill = 'black'));

def diviveIntervention(event):
	x = event.x//kSize;
	y = event.y//kSize;
	if board[x][y] == 1:
		board[x][y] = 0;
	else:
		board[x][y] = 1;
	redraw();

def makeTurn():
	global board;
	global nboard;
	for x in range(kBoardWidth):
		for y in range(kBoardHeight):
			neighbours = 0;
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
			neighbours = board[xplus][yplus] + board[xplus][y] + board[xplus][yminus] + board[x][yplus] + board[x][yminus] + board[xminus][yplus] + board[xminus][y] + board[xminus][yminus];
			if neighbours == 3:
				nboard[x][y] = 1;
			elif neighbours != 2:
				nboard[x][y] = 0;
			else:
				nboard[x][y] = board[x][y]
	board, nboard = nboard, board;

def loop(*args):
	if state:
		makeTurn();
		redraw();
		canvas.after(10, func=loop);

def switchState(*args):
	global state;
	state = not state;
	if state:
		loop();
def save(*args):
	plistlib.writePlist(board, "sav.plist");

canvas.bind("<Button-1>",diviveIntervention);
canvas.bind("<Button-3>",switchState);
canvas.bind("<Button-2>", save);
canvas.mainloop();
