n = int(input())
a = [1, 2, 4]
for i in range (3, 31):
	a.append(a[i-1] + a[i-2] + a[i-3])
print(a[n-1])
