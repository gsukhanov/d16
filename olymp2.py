n = int(input())
A = [][]
counter = 0
for i in range(n):
	for j in range(n):
		A[i][j] = input()
		if A[i][j] == "C":
			counter += 1
B = [][]
counterhalf = 0
for i in range(n):
	for j in range(n):
		if A[i][j] == "C":
			counterhalf += 1
		if counterhalf == counter // 2:
			m = i
			k = j
C = [][]
for i in range(n):
	for j in range(n):
		if i < m or i == m and j <= k:
			C[i][j] = 1
		else:
			C[i][j] = 2
print(C)
