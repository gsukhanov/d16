import random
c=0
for n in range (100000,1000000):
	array = []
	while n > 0:
		x = n % 10
		array.append(x)
		n = n // 10
	a=array[1]+array[2]+array[0]
	b=array[4]+array[5]+array[3]
	if a==b: 
		c=c+1
print(c)

