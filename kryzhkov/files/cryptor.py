import random
f_read = open('text.txt', 'r')
k_read = open('book2.txt', 'r')
f_write = open('crypt.txt', 'w')
a = []
i = []
for line in f_read:
    line = line.strip()
    l = line.split(' ')
    a += l
p = 0
s = '0'

for line in k_read:
    line = line.strip()
    l = line.split(' ')
    i += l
f_read.close()
f_read.close()
for x in range(len(a)):
  f_write.write(a[x])
  f_write.write(' ')
  for y in range(x+1):
    l = random.randrange(50000)
    if p == 9:
      s = i[x+y+l].capitalize()
      f_write.write(s)
    else:
      f_write.write(i[x+y+l])

    if (y+x) % 5 == 0:
      f_write.write('.')
      p = 9
    elif (y+x) % 6 == 0:
      f_write.write(',')
      p = 0
    else: 
      p = 0

    f_write.write(' ')
