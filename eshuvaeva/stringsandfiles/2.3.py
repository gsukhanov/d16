file1 = str(input())
file2 = str(input())
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	r = line.translate(str.maketrans({"o":"0"}))
f_read.close()
f_read = open(file2, 'w')
f_read.writelines(r)
f_read.close()

f_read = open(file2, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()
