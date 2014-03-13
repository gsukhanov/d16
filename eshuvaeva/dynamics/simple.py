n = int(input())
a = []
for i in range(2 * n):
	a.append(1)
def fib(n):
	if n == 0 or n == 1:
		return 1
	elif a [n] != 1:
		return a[n]
	elif n % 2 == 1:
		a[n] = fib(n // 2)-fib(n // 2-1)
	elif n % 2 == 0:
		a[n] = fib(n // 2) + fib(n // 2-1)
	return a[n]
k = fib(n)
print(k)