n = int(input("input a number, please: "))
array = []
while n > 0:
  x = n % 10
  array.append(x)
  n = n // 10
print (array)

