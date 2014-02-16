n, k = int(input()), int(input())

row = [1] * (k + 1)
for i in range(n):
    for j in range(1, k + 1):
        row[j] += row[j - 1]

print(row[-1])



