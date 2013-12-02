x = []
n = int(input("input a number"))

while n > 0:
	a = n % 10
	x.append(a)
	n = n // 10

print (x)
