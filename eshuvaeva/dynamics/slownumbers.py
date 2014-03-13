n = int(input())
a = []
for i in range(n):
	a.append(1)
def count(n):
	if n == 0:
		return 0
	if n == 1:
		return 9
	if n == 2:
		return 26
	elif a[n-1] != 1:
		return a[n -1] * 3 - 2
	else:
		a[n-1] = (count(n -2) * 3 + 1) * 3 -2
		return a[n -1]
k = count(n)
print(k)
