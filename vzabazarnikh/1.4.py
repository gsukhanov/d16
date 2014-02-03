n = input()

f = open (n, "r")
d = 0
a = f.readlines()
g = 0
for k in a:
	words = k.split()
	for h in range(len(words)):
		x = words[h]
		f = len(x)
		
		t = 0
		
		for t in range(f//2):
			if x[t] != x[-t]:
				t = 1

		if t = 0:
			g = g + 1

print (g)

			


