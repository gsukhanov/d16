# 0 - вправо, 1 - влево
n = int(input())
F = []
for s in range(n):
	F.append(int(input()))
B = F
for i in range(n):
	for j in range(n):
		if B[j] < B[j + 1]:
			B[j] = 1
			B[j + 1] = 0 
counter = 0
while F != B:
	i = 0
	while i < n - 1:
		if F[i] < F[i + 1]:
			F[i] = 1
			F[i + 1] = 0
			i +=1 
		i += 1
	counter += 1
print(counter)  
