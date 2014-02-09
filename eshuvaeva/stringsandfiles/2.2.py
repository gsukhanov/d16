file1 = str(input())
file2 = str(input())
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
	r = line[::-1]
print(r)
f_read.close()
f_read = open(file2, 'r')
f_read = r
