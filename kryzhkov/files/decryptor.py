import random
f_read = open('crypt.txt', 'r')
f_write = open('decrypt.txt', 'w')
a = []
i = []
for line in f_read:
    line = line.strip()
    l = line.split(' ')
    a += l
f_read.close()
f_write.write(a[0])
f_write.write(' ')
r = 0
for x in range(2,len(a)-2):
    r = r+x
    if r < len(a):
        f_write.write(a[r])
        f_write.write(' ')


