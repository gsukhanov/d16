n = int(input())
a = []
for i in range(1,n+1):
  y = int(input())
  a.append(y)
x = a
for j in range(n):
  for m in range(n):
    if x[m] < x[m + 1]:
      x[m] = 1
      x[m + 1] = 0    
k=0
while a != x:
  p = 0
  while p < len(a)-1:
    if a[p] < a[p+1]:
      a[p] = 1
      a[p+1] = 0
      p = p + 1
    p = p+1
  k += 1
print(k)
