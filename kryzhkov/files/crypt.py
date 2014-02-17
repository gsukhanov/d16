f_read = open('text.txt', 'r')
k_read = open('book2.txt', 'r')
f_write = open('crypt.txt', 'w')
a = []
i = []
for line in f_read:
    line = line.strip()
    l = line.split(' ')
    a += l

for line in k_read:
    line = line.strip()
    l = line.split(' ')
    i += l
f_read.close()
f_read.close()
for x in range(len(a)):
	f_write.write(a[x])
	f_write.write(' ')
	f_write.write(i[x+2000])
