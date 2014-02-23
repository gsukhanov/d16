n = int(input())
m = 0
def check(i,j):
	k = 0
	if i == 1 and j <= 9 and j >= 0:
		k = k + 1
	elif i==1 and (j>9 or j < 0):
		k = 0
	else:
		k = check(i-1,j) + check(i-1,j-1) + check(i-1, j - 2) + check(i - 1, j -3) + check(i-1,j - 4) + check(i -1, j -5) + check(i-1,j-6) + check(i-1, j - 7) + check(i-1, j -8) + check(i -1, j-9)
	return(k)

for j in range(9*n + 1):
	f = check(n,j)
	m = m + f * f
print(m)
