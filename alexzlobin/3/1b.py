kolvo=0
for z in range (000000,1000000):
	c=[]
	for _ in range(6):
		k=z%10
		c.append(k)
		z=z//10
	if c[0] + c[1]+c[2] == c[3]+c[4]+c[5]:
		kolvo+=1
print(kolvo)

