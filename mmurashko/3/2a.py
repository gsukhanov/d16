a = int(input())
array = []
x = []
for i in range(1,a+1):
  y = int(input())
  array.append(y)
  x.append(y)
for oi in range(0,a-1):
  for op in range(0,a-1):
    if x[op] < x[op+1]:
      x[op] = 1
      x[op+1] = 0     
print(x)
kolichestvo=0
while array != x:
  position = 0
  while position < len(array)-1:
    if array[position] < array[position+1]:
      array[position] = 1
      array[position+1] = 0
      position = position + 1
    position = position+1
  kolichestvo = kolichestvo+1
print(kolichestvo)
