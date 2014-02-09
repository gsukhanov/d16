n = int(input())

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)


for m in range(1,n,1):
	for k in range(1,m,1):
		d = factorial(m)
		j = factorial(k)
		h = m - k
		u = factorial(h)
		t = 1/(((n - 1)* d)/(j * u))
		print(t)
