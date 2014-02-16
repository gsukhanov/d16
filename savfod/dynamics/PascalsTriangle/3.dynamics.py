n, k = int(input()), int(input())

data = []
for i in range(n + 1):
    data.append([1] * (k + 1))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        data[i][j] = data[i-1][j] + data[i][j-1]

print(data[-1][-1])
