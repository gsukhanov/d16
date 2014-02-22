a = int(input())
b = int(input())
def tr(i,j):
	k = 0
	if i < j or (i + j) % 2 == 1:
		k = k
	elif i == j:
		k = k + 1
	elif j == 0:
		k == k + tr(i - 1, 1)
	else:
		k = k + tr(i - 1, j - 1)+tr(i-1,j+1)
	return k
print(tr(a + 1,b + 1))
