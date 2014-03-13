n = int(input())
a = []
for t in range(n):
    t = list(map(int, input().split()))
    a.append(t)
for i in range(len(a)):
    m = i
    for j in range(i + 1, len(a)):
        if a[j][1] > a[m][1] or (a[j][1] == a[m][1] and a[j][0] < a[m][0]):
            m = j
            a[m], a[i] = a[i], a[m]
     
for k in range(len(a)):
    print(a[k][0], a[k][1])