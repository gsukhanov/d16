import random
c=0
for n in range (100000,1000000):
	a = []
	while n > 0:
		m = n % 10
		a.append(m)
		n = n // 10
	x=a[1]+a[2]+a[0]
	y=a[4]+a[5]+a[3]
	if x==y: 
		c=c+1
print(c)
