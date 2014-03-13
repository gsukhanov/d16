n = int(input())
a = []
for i in range(n):
	a.append(1)
def fib(n):
	if n == 2 or n == 1:
		return 1
	elif a[n-1] != 1:
		return a[n-1]
	else:
		a[n-1] = fib(n -1)+fib(n-2)
		return a[n -1]
k = fib(n)
print(k)