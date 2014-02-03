n = input()

f = open (n, "r")



outfile = open(outfilename, 'w+');





d = 0
g = 0
for k in f:
	words = k.split()
	x = words[0]
	for h in range(len(words)):
		g = words[h + 1]
		if x != g:
			outfile.write(str(g))

		x = g

outfile.seek(0);
print (outfile.read());