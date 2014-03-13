n = int(input())
a = []
for i in range(n * 2):
	a.append(1)
r = []
for s in range(n * 2):
	r.append(1)
def one(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	elif a[n] != 1:
		return a[n]
	else:
		a[n] == zero(n-1)
		return a[n]
def zero(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	elif r[n] != 1:
		return r[n]
	else:
		r[n] = zero(n - 1) + one(n - 1)
		return r[n]
g = zero(n) + one(n)
print(g)
